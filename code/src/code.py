import time
import uasyncio
from machine import ADC, Pin, PWM

# from DCMotor import DCMotor
from motor_control import MotorFader

PWM_FREQUENCY = 1000
POT_THRESHOLD = 200
PWM_LOWER = 62000
PWM_FULL = 62000


enable = PWM(Pin(19))
enable.freq(PWM_FREQUENCY)
pin12 = Pin(12, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
adcPin = ADC(Pin(28))

fader = MotorFader(pin12, pin13, enable, adcPin)

def motorMove(target):
    if target < fader.potentiometer.read_u16() - POT_THRESHOLD:
        fader.forward(PWM_FULL)
        while target < (fader.potentiometer.read_u16() + POT_THRESHOLD):
            pass
        fader.stop()
    elif target > fader.potentiometer.read_u16() + POT_THRESHOLD:
        fader.backward(PWM_FULL)
        while target < (fader.potentiometer.read_u16() + POT_THRESHOLD):
            pass
        fader.stop()

def setTargetMinMax(target):
    if target > fader.upper_limit:
        target = fader.upper_limit
    if target < fader.lower_limit:
        target = fader.lower_limit
    return target

def checkCurrentPosition(lastPotPos):
    currentPotPos = fader.potentiometer.read_u16()
    if (lastPotPos < currentPotPos - POT_THRESHOLD) or (lastPotPos > currentPotPos + POT_THRESHOLD ):
        lastPotPos = currentPotPos
    return lastPotPos

motorLimits = fader.calibration(PWM_FULL)


while True:
    pass
