try:
    import RPi.GPIO as GPIO # type: ignore
except ImportError:
    print("RPi.GPIO module not found. Please install it using 'pip install RPi.GPIO'.")
    GPIO = None
from common import *

class RpiGpio:
    def __init__(self):
        self.init()


    def init(self):
        if GPIO is None:
            print("RPi.GPIO module is not available.")
            return
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)


    def deinit(self):
        if GPIO:
            GPIO.cleanup()


    def pinMode(self, pin: int, state: bool, pullUpDown: bool|None = None):
        if GPIO is None:
            print("RPi.GPIO module is not available.")
            return
        _state      = None
        _pullUpDown = None

        # Mapping with INPUT OUTPUT macro with GPIO.IN GPIO.OUT
        if state == INPUT:
            _state = GPIO.IN
        elif state == OUTPUT:
            _state = GPIO.OUT
        else:
            raise Exception("Wrong pin status!!")

        # Mapping with PULL_UP PULL_DOWN macro with GPIO.PUD_UP GPIO.PUD_DOWN
        if pullUpDown == PULL_UP:
            _pullUpDown = GPIO.PUD_UP
        elif pullUpDown == PULL_DOWN:
            _pullUpDown = GPIO.PUD_DOWN
        else:
            _pullUpDown = GPIO.PUD_OFF

        if pullUpDown != None:
            GPIO.setup(pin, _state, pull_up_down = _pullUpDown)
        elif state == OUTPUT:
            GPIO.setup(pin, _state, initial = GPIO.LOW)
        else:
            GPIO.setup(pin, _state)


    def digitalRead(self, pin: int):
        if GPIO is None:
            return LOW
        state = GPIO.input(pin)
        return state


    def digitalWrite(self, pin: int, state: bool):
        if GPIO is None:
            return
        _state = None

        # Mapping with HIGH LOW macro with GPIO.HIGH GPIO.LOW
        if state == HIGH:
            _state = GPIO.HIGH
        elif state == LOW:
            _state = GPIO.LOW
        else:
            raise Exception("Wrong pin status!!")

        GPIO.output(pin, _state)
