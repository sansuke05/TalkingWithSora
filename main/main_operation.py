# -*- coding: utf-8 -*-

import os
import recording_voice
import transcribe
import responder
import speaker
from system import system_voice


ENV_PATH = '../config/TalkWithCharaProject-6df0a95a6e30.json'


class CommandExecutionFailed(Exception):
    def __str__(self):
        return 'soxコマンドの実行に失敗しました'

def main():
    print('-------------------------------------------')
    print('Welcome to communication system with Sora')
    print('Version: 0.1.0\nCreated by sansuke05')
    print('-------------------------------------------')
    print('Starting App...\n')

    # init
    # 環境変数設定
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = ENV_PATH

    # LED制御スレッドの生成

    while True:
        print('> ', end='')
        command = input()
        # 音声認識開始処理
        if command == 'start':
            # 音声認識開始音声の再生
            system_voice.play(command))

            # 録音処理
            recording_voice.record()

            # サンプリングレートの変換
            command = 'sox recordedVoice/tmp.wav -r 16k recordedVoice/tmp_converted.wav'
            if(os.system(command) != 0):
                raise CommandExecutionFailed()
            
            # 音声認識
            transcribe.transribe_file()

            # 応答
            f = open('./generatedText/tmp.txt')
            input_text = f.readline().replace('\n','')
            f.close()
            response_text = responder.pattern_response(input_text)
            print(response_text)

            # 発話
            speaker.talk(response_text)
        
        # 終了条件
        if command == 'exit':
            print('Exiting app...')
            break
# [END main]


if __name__ == '__main__':
    main()