import sys
import threading
import numpy as np
import sounddevice as sd
import soundfile as sf
from typing import List, Optional
from src.model.detector import WakeWordDetector


class AudioBuffer:
    """
    Real-time sliding buffer for wake word detection.
    """
    def __init__(self, detector: WakeWordDetector, duration: float = 0.25, buffer_size: int = 4):
        self.detector = detector
        self.duration = duration
        self.buffer: List[Optional[np.ndarray]] = [None] * buffer_size
        self.stream = None
        self.lock = threading.Lock()
        self._index = 0

    def add_to_buffer(self, data: np.ndarray) -> None:
        """
        Adds a chunk to the sliding buffer and triggers detection.
        """
        with self.lock:
            self.buffer.pop(0)
            self.buffer.append(data.copy())

            if None not in self.buffer:
                self.process_predict()

    def process_predict(self) -> None:
        """
        Runs prediction on concatenated buffer content.
        """
        audio_data = np.concatenate(self.buffer)
        prob = self.detector.predict(audio_data)
        if prob > self.detector.threshold:
            print(f"✅ Wake word detected with probability: {prob:.2f}")

    def callback(self, indata, frames, time, status) -> None:
        data = indata[:, 0]
        threading.Thread(target=self.add_to_buffer, args=(data,)).start()

    def start_listen(self) -> None:
        """
        Starts continuous listening stream.
        """
        self.stream = sd.InputStream(callback=self.callback,
                                     channels=1,
                                     samplerate=44100,
                                     blocksize=int(44100 * self.duration))
        self.stream.start()
        print("🎧 Listening for wake word...")
        while True:
            sd.sleep(int(self.duration * 1000))

    def stop_listen(self) -> None:
        if self.stream:
            self.stream.stop()
        sys.exit(0)
