# -*- coding: utf-8 -*-

import random
import re

# パターンマッチに失敗した場合こちらを返す
def random_response():
    #f = open('/home/pi/projects/SoraTwitterBot/dictionary/random.txt')
    f = open('./dictionary/random.txt')
    buffar = f.readlines()
    f.close()

    # ランダムに1文選択
    phrase = random.choice(buffar)
    phrase = phrase.replace('\n','')
    
    return phrase


def pattern_response(text):
    f = open('./dictionary/pattern.txt')
    
    buffar = f.readlines()
    f.close()

    # パターンマッチ
    for line in buffar:
        phrase = line.replace('\n','').split(':')
        _pattern = phrase[0]
        _responses = phrase[1].split(',')
        _response = random.choice(_responses)
        m = re.search(_pattern, text)

        if m:
            return _response

    # パターンがない場合
    return random_response()


# テストコード
if __name__ == '__main__':
    f = open('./generatedText/tmp.txt')
    input_text = f.readline().replace('\n','')
    f.close()

    response_text = pattern_response(input_text)
    print(response_text)