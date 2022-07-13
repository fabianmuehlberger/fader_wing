'''Module is uesed for evaluation purposes and can be used as a stand alone script  '''

import time
import utime
from motor_control import MotorFader
from machine import Pin, PWM, ADC

if __name__ == " __main__":

    PWM_FREQUENCY = 65000

    enable = PWM(Pin(19))
    enable.freq(PWM_FREQUENCY)
    pin12 = Pin(12, Pin.OUT)
    pin13 = Pin(13, Pin.OUT)
    adcPin = ADC(Pin(28))

    fader = MotorFader(pin12, pin13, enable, adcPin)


def evaluate_movement_duration(duty):
    '''Test the total movement duration from one side to the other. Duty Cycle used is 62000, 9V supply voltage'''
    print("initial Position =", adcPin.read_u16())

    time.sleep(1)
    while adcPin.read_u16() < PWM_FREQUENCY:
        fader.move_forward(duty)
    fader.stop()
    print("Moved to first position ", adcPin.read_u16())

    time.sleep(1)
    timestamp = utime.ticks_ms()
    while adcPin.read_u16() > 300:
        fader.move_backward(duty)
    print("Moved to first position ", adcPin.read_u16())
    fader.stop()
    new_time = utime.ticks_ms()
    delay_time = new_time - timestamp

    print("time = ", delay_time / 1000)
