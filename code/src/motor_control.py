'''motor_ontrol'''
import time

SHORT_SLEEP = 0.1

class MotorFader:
    '''Controlls movement of the motorfader including methods for setting the upper and lower limit of the fader'''
    def __init__(self, forward, backward, enable_pin, potentiometer):
        self.potentiometer = potentiometer
        self.upper_limit = 0
        self.lower_limit = 0
        self.speed = 0
        self.forward=forward
        self.backward=backward
        self.enable_pin = enable_pin

    def move_forward(self, speed):
        '''move motor forward'''
        self.speed = speed
        self.forward.value(1)
        self.backward.value(0)
        self.enable_pin.duty_u16(speed)

    def move_backward(self, speed):
        '''move motor backwards'''
        self.speed = speed
        self.forward.value(0)
        self.backward.value(1)
        self.enable_pin.duty_u16(speed)

    def stop(self):
        '''set duty and forward and backward pin to zero'''
        self.forward.value(0)
        self.backward.value(0)
        self.enable_pin.duty_u16(0)

    def calibration(self, speed):
        '''read the upper and lower limit of the potentiometer amd setting it as the limits to improve the accuracy'''
        self.stop()
        time.sleep(SHORT_SLEEP)

        self.forward(speed)
        lower = self.get_limit('upper')
        self.stop()
        time.sleep(SHORT_SLEEP)

        self.backward(speed)
        upper = self.get_limit('lower')
        self.stop()
        time.sleep(SHORT_SLEEP)

        return upper, lower

    def get_limit(self, limit):
        ''' read potentiometer value at position'''
        potentiometer_values = []
        for _ in range(1, 1000):
            potentiometer_values.append(self.potentiometer.read_u16())
            time.sleep(0.001)

            if limit == "upper":
                self.upper_limit = max(potentiometer_values)
            if limit == "lower":
                self.lower_limit = max(potentiometer_values)
