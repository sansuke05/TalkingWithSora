# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import threading
import concurrent.futures


class GPIOOperation():

    def __init__(self):
        self.stop_event = threading.Event() #停止用のフラグ
        self.thread = None
    
    def setUp(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)

    def start_thread(self, mode):
        if mode == 'wait':
            self.thread = threading.Thread(target=self.blink_led)
        else:
            self.thread = threading.Thread(target=self.blink_led_frequently)
        self.thread.start()
    
    def blink_led(self):
        while not self.stop_event.is_set():
            self.light_on()
            time.sleep(1)
            self.light_off()
            time.sleep(1)

    def blink_led_frequently(self):
        while not self.stop_event.is_set():
            self.light_on()
            time.sleep(0.2)
            self.light_off()
            time.sleep(0.2)
    
    def light_on(self):
        GPIO.output(3, True)
    
    def light_off(self):
        GPIO.output(3, False)
    
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