# -*- coding: utf-8 -*-

import os
from subprocess import call

VOICE_DIR_PATH = u"./sora_voices/"

def talk(voice_file_name):
    path = VOICE_DIR_PATH + voice_file_name + '.mp3'
    print('Now playing...')
    #call(['afplay', path]) #This command work on macOS only.
    call(['aplay', path])

# テストコード
if __name__ == '__main__':
    voice_file_name = 'oyasumi1'
    talk(voice_file_name)