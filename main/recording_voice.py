# -*- coding: utf-8 -*-

import pyaudio
import wave

# Output file setting
OUT_FILE_PATH = 'recordedVoice/tmp.wav'

# Audio recording parameters
FORMAT = pyaudio.paInt16
RATE = 16000
CHUNK = 1024 * 2
RECORD_SECONDS = 5

def record():
    p = pyaudio.PyAudio()

    # 録音データ設定
    stream = p.open(
        format = FORMAT,
        # The API currently only supports 1-channel (mono) audio
        channels = 1,
        rate = RATE,
        input = True,
        frames_per_buffer = CHUNK,
    )

    # 録音開始
    print('start recording...')
    frame = []
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frame.append(data)
    
    print('Recording is done.')

    stream.stop_stream()
    stream.close()
    p.terminate()

    data = b''.join(frame)
    out = wave.open(OUT_FILE_PATH, 'w')
    out.setnchannels(1) # mono
    out.setsampwidth(2) # 16bits
    out.setframerate(RATE)
    out.writeframes(data)
    out.close()
# [END record()]


if __name__ == '__main__':
    record()