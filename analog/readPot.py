from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(35))
pot.atten(ADC.ATTN_11DB)
while True:
    potVal = pot.read()
    print(potVal)
    sleep(0.1)
