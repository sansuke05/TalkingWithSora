# -*- coding: utf-8 -*-

import time
import threading
import concurrent.futures


class GPIOOperation():

    def __init__(self):
        self.stop_event = threading.Event() #停止用のフラグ
        self.thread = None
    
    def start_thread(self, mode):
        if mode == 'wait':
            self.thread = threading.Thread(target=self.blink_led)
        else:
            self.thread = threading.Thread(target=self.blink_led_frequently)
        self.thread.start()
    
    def blink_led(self):
        while not self.stop_event.is_set():
            print("light on")
            time.sleep(1)
            print("light off")
            time.sleep(1)

    def blink_led_frequently(self):
        while not self.stop_event.is_set():
            print("light on")
            time.sleep(0.2)
            print("light off")
            time.sleep(0.2)
    
    def light_on(self):
        print("light on")
    
    def light_off(self):
        print("light off")
    
    def stop(self):
        self.stop_event.set()
        self.thread.join()



# テストコード
if __name__ == '__main__':
    gpio = GPIOOperation()
    gpio.start_thread('wait')

    for i in range(3):
        print('---------main----------')
        time.sleep(1)
    
    gpio.stop()
    gpio.light_on()

    for i in range(3):
        print('---------main----------')
        time.sleep(1)
    
    del gpio
    gpio = GPIOOperation()
    gpio.start_thread('recognition')
    
    for i in range(3):
        print('---------main----------')
        time.sleep(1)
    
    gpio.stop()
    gpio.light_on()

    for i in range(3):
        print('---------main----------')
        time.sleep(1)
    
    del gpio
    gpio = GPIOOperation()
    gpio.start_thread('wait')

    for i in range(3):
        print('---------main----------')
        time.sleep(1)
    
    gpio.stop()
    gpio.light_off()

    time.sleep(3)
    print("finish")