'''Module is uesed for evaluation purposes. '''
import motor_control


'''Test the total movement duration from one side to the other. Duty Cycle used is 62000, 9V supply voltage'''
def evaluate_movement_duration(duty)
    print("initial Position =", adcPin.read_u16())

    time.sleep(1)
    while adcPin.read_u16() < 65000:
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