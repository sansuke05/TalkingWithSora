# -*- coding: utf-8 -*-

import os
import recording_voice
import transcribe
import responder

ENV_PATH = '../config/TalkWithCharaProject-6df0a95a6e30.json'


def main():
    print('-------------------------------------------')
    print('Welcome to communication system with Sora')
    print('Version: 0.0.1\nCreated by sansuke05')
    print('-------------------------------------------')
    print('Starting App...\n')

    # init
    # 環境変数設定
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ENV_PATH

    while True:
        print('> ', end='')
        command = input()
        # 音声認識開始処理
        if command == 'start':
            # 録音処理
            recording_voice.record()
            # 音声認識
            transcribe.transribe_file()
            # 応答
            f = open('./generatedText/tmp.txt')
            input_text = f.readline().replace('\n','')
            f.close()

            response_text = responder.pattern_response(input_text)
            print(response_text)
            # 発話
        
        # 終了条件
        if command == 'exit':
            print('Exiting app...')
            break
# [END main]


if __name__ == '__main__':
    main()