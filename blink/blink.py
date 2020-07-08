from machine import Pin
from time import sleep
#import serial
led = Pin(2,Pin.OUT)
while True:
    led.value(not led.value())
    #print('blink')
    sleep(0.1)
