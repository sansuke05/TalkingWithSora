# !/usr/bin/env python
# coding: utf-8
import argparse
import io
import os
import sys
import codecs
import datetime
import locale

def transribe_file(speech_file):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        sample_rate_hertz=16000,
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='ja-JP')


    # 短い音声の場合recognize()メソッドを使用
    # 長い音声の場合はlong_running_recognize()メソッドも用意されている
    operation = client.recognize(config, audio) 

    print('Waiting for operation to complete...')
    result = operation.results[0]

    d = datetime.datetime.today()
    today = d.strftime("%Y%m%d-%H%M%S")
    path = 'generatedText/output{}.txt'.format(today)
    fout = codecs.open(path, 'a', 'utf-8')

    for alternative in result.alternatives:
        fout.write(u'{}\n'.format(alternative.transcript))
    fout.close()

if __name__ == '__main__':
    path = '../config/TalkWithCharaProject-6df0a95a6e30.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='file path for audio file to be recognized')
    args = parser.parse_args()
    transribe_file(args.path)