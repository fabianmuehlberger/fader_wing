import sys
import rp2
from machine import ADC, Pin, PWM
import time
# from DCMotor import DCMotor
from motorControl import *

PWM_FREQUENCY = 1000
POT_THRESHOLD = 200
PWM_LOWER = 62000
PWM_FULL = 62000


enable = PWM(Pin(19))
enable.freq(PWM_FREQUENCY)
pin1 = Pin(12, Pin.OUT)
pin2 = Pin(13, Pin.OUT)
adcPin = ADC(Pin(28))

dc_motor = DC_Motor(pin1, pin2, enable)
lin_pot = Lin_potentiometer(adcPin)

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
    
button = machine.Pin(11,machine.Pin.IN, machine.Pin.PULL_DOWN)
button.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=ISR_button)


def motorMove(motor):
    
    if target < linPot.read_u16() - POT_THRESHOLD:
        motor.driveUp(45000)
        while target < (linPot.read_u16() + POT_THRESHOLD):
             pass   
        motorStop()
    elif target > linPot.read_u16() + POT_THRESHOLD:            
        motor.driveDown(45000)
        while target < (linPot.read_u16() + POT_THRESHOLD):
            pass
        motorStop()
    return 
    
def setTargetMinMax(lim, target):
    if target > lim.upper:
        target = lim.upper
    if target < lim.lower:
        target = lim.lower
    return target
        
def checkCurrentPosition(lastPotPos):
    currentPotPos = linPot.read_u16()
    if (lastPotPos < currentPotPos - POT_THRESHOLD) or (lastPotPos > currentPotPos + POT_THRESHOLD ):
        lastPotPos = currentPotPos
    return lastPotPos

motorLimits = calibration(dc_motor, PWM_FULL)
buttonState = button.value()

def buttonPress():
    posOld = linPot.read_u16()
    posNew = checkCurrentPosition(posOld)
    if posOld != posNew:
        posOld = posNew
    print('current position = ', posNew)
    return posOld

while True:

    dc_motor.forward(PWM_FULL)
    time.sleep(0.5)
    dc_motor.stop()
    time.sleep(0.1)

    dc_motor.backward(PWM_FULL)
    time.sleep(0.5)
    dc_motor.stop()
    time.sleep(0.1)
    pass

