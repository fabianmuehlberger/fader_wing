'''motor_ontrol'''
import time
from machine import Pin, PWM

PWM_FULL = 65535
PWM_LOWER = 45000
PWM_HALF = 32222

SHORT_SLEEP = 0.1

class DCMotor:
    '''motorControl'''
    def __init__(self, pin1, pin2, enable_pin):
        self.speed = 0
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin = enable_pin

    def forward(self, speed):
        '''move motor forward'''
        self.speed = speed
        self.pin1.value(1)
        self.pin2.value(0)
        self.enable_pin.duty_u16(speed)

    def backward(self, speed):
        '''move motor backwards'''
        self.speed = speed
        self.pin1.value(0)
        self.pin2.value(1)
        self.enable_pin.duty_u16(speed)

    def stop(self):
        '''stop motor'''
        self.pin1.value(0)
        self.pin2.value(0)
        self.enable_pin.duty_u16(0)
        print("Pin 12 = ", self.pin1(), "Pin 13", self.pin2())

def calibration(motor, speed, pin):
    '''calibrate motor limits'''
    motor.stop()
    time.sleep(SHORT_SLEEP)

    motor.forward(speed)
    lower = LinPotentiometer.get_limit('upper')
    motor.stop()
    time.sleep(SHORT_SLEEP)

    motor.backward(speed)
    upper = LinPotentiometer.get_limit('lower')
    motor.stop()
    time.sleep(SHORT_SLEEP)

    return upper, lower


class LinPotentiometer:
    '''Linear Potentiometer'''
    def __init__(self, pin):
        upper_limit = 0
        lower_limit = 0
        self.pin = pin
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit

    def get_limit(self, limit):
        ''' read potentiometer value at position'''
        potentiometer_values = []
        for i in range(1, 1000):
            potentiometer_values.append(linPot.read_u16())
            time.sleep(0.001)

            max_number= max(potentiometer_values)
            min_number = min(potentiometer_values)
            delta = max_number- min_number

            if limit == "upper":
                return min_number
            return max_number
            