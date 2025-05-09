import numpy as np
from src.model.detector import WakeWordDetector


def test_preprocess_shape():
    dummy_audio = np.random.randn(44100)
    detector = WakeWordDetector(model_path="saved_model/WWD_v3.h5")
    features = detector.preprocess(dummy_audio)
    assert features.ndim == 3
