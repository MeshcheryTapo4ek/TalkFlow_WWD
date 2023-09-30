import threading

import sounddevice as sd
import numpy as np
import librosa
import tensorflow as tf

import soundfile as sf

# Загрузить модель
model = tf.keras.models.load_model('saved_model/WWD.h5')


# Функция для предварительной обработки аудио данных
def preprocess_audio_data(audio_clip):
    return np.array([librosa.feature.mfcc(y=audio_clip, sr=44100, n_mfcc=20)])

def process_data_and_predict(audio_data):
    audio_data = preprocess_audio_data(audio_data)
    #print(f"Shape of the audio data: {audio_data.shape}");

    prediction = model.predict(audio_data, verbose=0)

    print(f"probabilyty: {prediction[0]}" );


def callback(indata, frames, time, status):
    # Создаем и запускаем отдельный поток
    threading.Thread(
        target=process_data_and_predict,
        args=(indata[:, 0],)
        ).start()

#duration = 1  # seconds
#with sd.InputStream(callback=callback,
#                    channels=1,
#                    samplerate=44100,
#                    blocksize=int(44100 * duration)):
#    while True:
#        sd.sleep(int(duration*1000))

audio_file_path = 'audio_data/Дубина0.wav'

# Чтение аудиофайла с помощью librosa
audio_data1, sample_rate = librosa.load('segment_0.wav', sr=44100)
audio_data2, sample_rate = librosa.load('segment_1.wav', sr=44100)
audio_data3, sample_rate = librosa.load('segment_2.wav', sr=44100)
audio_data4, sample_rate = librosa.load('segment_3.wav', sr=44100)

def break_audio(audio_data):
    sample_rate = 44100
    # Разбиваем аудиоданные на 4 равные части
    num_segments = 4
    segment_length = len(audio_data) // num_segments

    # Создаем и сохраняем каждую часть в отдельный файл
    for i in range(num_segments):
        start_sample = i * segment_length
        end_sample = (i + 1) * segment_length

        # Имя файла для сохранения
        output_file_name = f'segment_{i}.wav'

        # Вырезаем сегмент из аудиоданных
        segment = audio_data[start_sample:end_sample]

        # Сохраняем сегмент в файл
        sf.write(output_file_name, segment, sample_rate)

        print(f"Сегмент {i} сохранен в {output_file_name}")

x4_buffer_data = np.concatenate([audio_data1,audio_data2,audio_data3,audio_data4])

sf.write('output.wav', x4_buffer_data, 44100)
process_data_and_predict(x4_buffer_data)
