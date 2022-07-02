# type: ignore
# pylint: disable-all

def ISR_button(pin):
    global buttonState
    button.irq(handler = None)

    if (button.value() == 1) and (buttonState == 0):
        buttonState = 1
        print("ON")

    elif (button.value() == 0) and (buttonState == 1):
        buttonState = 0
        print("OFF")
    button.irq(handler=ISR_button)

    

button = Pin(11,Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=ISR_button)

