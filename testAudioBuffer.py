import sys
import threading

import sounddevice as sd
import numpy as np
import librosa
import soundfile as sf
import tensorflow as tf


class AudioBuffer:
    def __init__(self, duration):
        self.i=0
        # Ваш список для хранения данных аудио
        # размером с четыре последних прочитанных фрагмента по duration сек
        self.buffer = [None, None, None, None]
        self.full = False
        self.duration = duration

        #модель для обработки
        self.model = tf.keras.models.load_model('saved_model/WWD_v3.h5')


    def add_to_buffer(self, data):
        # Удаляем старые данные
        self.buffer.pop(0)
        # добавляем новые данные в буфер
        self.buffer.append(data.copy())

        if self.buffer[0] is not None:
            self.process_predict()
        else:
            print(" buffer isnt full")

    def process_predict(self):

        # there is some function which helps to test our buffer
        def save_test_():
            self.i += 1
            sf.write(f'pepe/output{self.i}_1_4.wav', self.buffer[0], 44100)
            sf.write(f'pepe/output{self.i}_2_4.wav', self.buffer[1], 44100)
            sf.write(f'pepe/output{self.i}_3_4.wav', self.buffer[2], 44100)
            sf.write(f'pepe/output{self.i}_4_4.wav', self.buffer[3], 44100)
            sf.write(f'pepe/output{self.i}.wav', x4_buffer_data, 44100)

        def preprocess_audio_data(audio_clip):
            # important n_mfcc
            return np.array([librosa.feature.mfcc(y=audio_clip, sr=44100, n_mfcc=5)])

        x4_buffer_data = np.concatenate(self.buffer)
        #save_test_()
        prediction = self.model.predict(preprocess_audio_data(x4_buffer_data), verbose=0)
        if(prediction[0] > 0.80):
            print(f"Detected! With probability: {prediction[0]}" );

    def start_listen(self):

        def continuous_audio_collection():
            while True:
                sd.sleep(int(self.duration * 1000))


        self.stream = sd.InputStream(callback=self.callback,
                                     channels=1,
                                     samplerate=44100,
                                     blocksize=int(44100 * self.duration))
        self.stream.start()
        continuous_audio_collection()

    def stop_listen(self):
        print(" Stopping the program...")
        if self.stream:
            self.stream.stop()
        sys.exit(0)

    def callback(self, indata, frames, time, status):

        def func():
            data = (indata[:, 0])
            self.add_to_buffer(data)

        self.thread = threading.Thread(target=func)
        self.thread.start()





audio_buffer = AudioBuffer(duration=0.25)
audio_buffer.start_listen()


