import sys
import threading

import sounddevice as sd
import numpy as np
import librosa
import soundfile as sf


# в Данном файле мы проверяем что буфер обрабатывает правильный звук и в буфере находятся верные данные
audio_data_list = []

for i in range(1, 40,4):
    audio_file_path = f'pepe/output{i}.wav'
    audio_data, _ = librosa.load(audio_file_path,
                                 sr=44100)
    audio_data_list.append(audio_data)


pepe = np.concatenate(audio_data_list)
sf.write('output.wav', pepe, 44100)