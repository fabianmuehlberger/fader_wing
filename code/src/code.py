import sys
import rp2
import time
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

def ISR_button(pin):         # button Interrupt handler
    global buttonState      # reference the global variable
    button.irq(handler = None) # Turn off the handler while it is executing
    
    if (button.value() == 1) and (buttonState == 0):  # button is active (High) and button State is currently Low
        buttonState = 1     # Update current state of switch
        print("ON")   
        
    elif (button.value() == 0) and (buttonState == 1): # button is not-active (Low) and button State is currently High
        buttonState = 0     # Update current state of switch
        print("OFF")      
    button.irq(handler=ISR_button)
    
button = Pin(11,Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=ISR_button)


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
    return 
    
def setTargetMinMax(lim, target):
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
