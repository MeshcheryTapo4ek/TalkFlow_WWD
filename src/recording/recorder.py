from pathlib import Path
import sounddevice as sd
from scipy.io.wavfile import write


def record_audio_and_save(save_dir: Path, prefix: str, n_times: int = 50, duration: float = 1.0) -> None:
    """
    Records short audio clips and saves them to WAV files.

    :param save_dir: Path to directory where audio will be saved.
    :param prefix: Prefix for file names (e.g., 'wakeword').
    :param n_times: Number of clips to record.
    :param duration: Duration of each recording in seconds.
    """
    save_dir.mkdir(parents=True, exist_ok=True)
    input("Press Enter to start recording...")

    for i in range(n_times):
        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        filename = save_dir / f"{prefix}_{i}.wav"
        write(str(filename), fs, recording)
        input(f"[{i+1}/{n_times}] Press Enter for next or Ctrl+C to stop.")
