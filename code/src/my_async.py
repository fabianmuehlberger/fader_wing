'''This Module is a example for using uasyncio and does not represent actual working code'''

import uasyncio
import machine
from machine import ADC, Pin, PWM


# settings

led = machine.Pin(25, machine.Pin.OUT)
btn = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)
adcPin = ADC(Pin(28))

async def blink(delay):
    while True:
        led.toggle()
        await uasyncio.sleep(delay)

async def wait_button():
    btn_prev = btn.value()
    while (btn.value() == 1) or (btn.value() == btn_prev):
        btn_prev = btn.value()
        await uasyncio.sleep(0.04)

async def main():
    
    uasyncio.create_task(blink(0.5)) 
    
    while True:
        await wait_button()
        print("value =", adcPin.read_u16())
    
    
    
uasyncio.run(main())



