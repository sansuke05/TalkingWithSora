# -*- coding: utf-8 -*-

import pyaudio

# Audio recording parameters
FORMAT = pyaudio.paInt16
RATE = 16000
CHUNK = 1024  # 100ms
RECORD_SECONDS = 3

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
    