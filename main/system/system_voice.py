# -*- coding: utf-8 -*-

from subprocess import call

START_SIGN = "system/start.mp3"
#START_SIGN = "start.mp3" テスト用

def play(mode):
    if mode == 'start':
        call(['mpg321', START_SIGN])


# テストコード
if __name__ == '__main__':
    command = 'start'
    play(command)