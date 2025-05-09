from pathlib import Path
from src.recording.recorder import record_audio_and_save


if __name__ == "__main__":
    record_audio_and_save(Path("audio_data"), prefix="wakeword", n_times=60)
    record_audio_and_save(Path("background_noise"), prefix="noise", n_times=200)
