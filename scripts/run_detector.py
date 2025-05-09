from src.model.detector import WakeWordDetector
from src.buffer.audio_buffer import AudioBuffer


if __name__ == "__main__":
    detector = WakeWordDetector(model_path="saved_model/WWD_v3.h5", threshold=0.8)
    buffer = AudioBuffer(detector=detector, duration=0.25)
    buffer.start_listen()
