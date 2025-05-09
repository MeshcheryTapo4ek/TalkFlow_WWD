import numpy as np
import librosa
import tensorflow as tf


class WakeWordDetector:
    """
    Loads a Keras model and provides prediction interface.
    """
    def __init__(self, model_path: str, threshold: float = 0.8):
        self.model = tf.keras.models.load_model(model_path)
        self.threshold = threshold

    def preprocess(self, audio_clip: np.ndarray, sample_rate: int = 44100, n_mfcc: int = 20) -> np.ndarray:
        """
        Extract MFCC features from raw audio.

        :param audio_clip: 1D NumPy array of audio samples.
        :return: 2D array for model input.
        """
        mfcc = librosa.feature.mfcc(y=audio_clip, sr=sample_rate, n_mfcc=n_mfcc)
        return np.expand_dims(mfcc, axis=0)

    def predict(self, audio_clip: np.ndarray) -> float:
        """
        Predict wake word probability.

        :param audio_clip: Raw audio array.
        :return: Probability from model.
        """
        features = self.preprocess(audio_clip)
        prediction = self.model.predict(features, verbose=0)
        return float(prediction[0][0])
