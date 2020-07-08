from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)
button = Pin(4,Pin.OUT)
while True:
    led.value(button.value())
    print('blink')
    sleep(0.1)
