from datetime import datetime
import time

from lcd20x4 import Lcd20x4
from rpigpio import RpiGpio

from utility import *
from common  import *
from pinDescription import *


# global hardware module library initilization
lcd  = Lcd20x4(LCD_MODULE_ADDRESS, LCD_MODULE_NO_OF_COLUMN, LCD_MODULE_NO_OF_ROW)
gpio = RpiGpio()


# global variables
cycleIndexPos = 0
cycleCounter  = 0

previousPosition = None
currentPosition  = None

ResetBtnReading  = None
buttonState      = None

powerDownTrigger = False
ResetTrigger     = False
isEepromReadNeed = True
cycleIndexPosMiddle = False

lastButtonState  = HIGH
debounceDelay    = 5000
lastDebounceTime = 0


# Introduction banner print
def startIntroPrint():
    lcd.write("SPRING LOADED", row = ROW_NO_0, center = True)
    lcd.write("SWITCH TESTER", row = ROW_NO_1, center = True)
    appVersion = getAppVersion()
    lcd.write(f"Version: {appVersion}", row = ROW_NO_3, padding = True)
    time.sleep(3)
    lcd.clean()
    time.sleep(0.5)
    lcd.turnOffBacklight()
    time.sleep(1)
    lcd.turnOnBacklight()
    time.sleep(1)


# This is the gpio initlization
def gpioInilitization():
    gpio.pinMode(ON_BOARD_LED_PIN, OUTPUT)

    gpio.pinMode(MICRO_SWITCH_S1_NC_PIN, INPUT)
    gpio.pinMode(MICRO_SWITCH_S1_NO_PIN, INPUT)
    gpio.pinMode(MICRO_SWITCH_S2_NC_PIN, INPUT)
    gpio.pinMode(MICRO_SWITCH_S2_NO_PIN, INPUT)

    gpio.pinMode(POWER_LINE_DETECT_PIN, INPUT)
    gpio.pinMode(RESET_PUSH_SWITCH_PIN, INPUT)

    gpio.pinMode(ON_BOARD_LED_PIN, OUTPUT)


# Time print function
def printCurrentTime(row: int):
    lcd.write(datetime.now().strftime('%I:%M:%S %p %d/%m/%y'), row = ROW_NO_0, padding = True)
    # time.sleep(0.1)


# Print the count value
def printCount(row: int, count: int):
    lcd.write(f"Count: {count}", row = row, padding = True)


#  This is the void setup() function just like Arduino code
def setup():
    global cycleIndexPos
    global previousPosition
    global cycleCounter

    startIntroPrint()
    gpioInilitization()
    createRtDbFile()

    if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
        previousPosition = POSITION_LEFT
        cycleIndexPos    = POSITION_LEFT

    if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
        previousPosition = POSITION_MIDDLE
        cycleIndexPos    = POSITION_MIDDLE

    if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
        previousPosition = POSITION_RIGHT
        cycleIndexPos    = POSITION_RIGHT

    ########## TEST BEGIN ###############
    if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and  gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN) and\
        gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN) and\
        gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
        previousPosition = POSITION_MIDDLE
        cycleIndexPos    = POSITION_MIDDLE
        print("Probably No switch found; All pin are HIGH ... !!")
    ########## TEST END## ###############

    cycleCounter = getCycleCount()
    printCount(row = ROW_NO_2, count = cycleCounter)

    gpio.digitalWrite(ON_BOARD_LED_PIN, LOW)


# This is the void loop() function just like Arduino code
def loop():
    global powerDownTrigger
    global isEepromReadNeed
    global previousPosition
    global cycleIndexPos
    global currentPosition
    global cycleCounter
    global cycleIndexPosMiddle
    global ResetBtnReading
    global lastButtonState
    global debounceDelay
    global buttonState
    global ResetTrigger
    global lastDebounceTime

    while True:
        if not powerDownTrigger:
            printCurrentTime(ROW_NO_0)

        # If power down condition happend
        if gpio.digitalRead(POWER_LINE_DETECT_PIN) == LOW:
            lcd.turnOffBacklight()
            lcd.clean()
            powerDownTrigger = True

            if not isEepromReadNeed:
                setCycleCount(cycleCounter)
                isEepromReadNeed = True
            continue
        else:
            lcd.turnOnBacklight()
            powerDownTrigger = False
            if isEepromReadNeed:
                cycleCounter = getCycleCount()
                lcd.write(" "*LCD_MODULE_NO_OF_COLUMN, row = ROW_NO_3)
                isEepromReadNeed = False

        # Reading the gpio pin for the switchs
        if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
            currentPosition = POSITION_LEFT
            lcd.write("Position Left  ", row = ROW_NO_1)

        if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
            currentPosition = POSITION_MIDDLE
            lcd.write("Position Middle", row = ROW_NO_1)

        if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
            currentPosition = POSITION_RIGHT
            lcd.write("Position Right ", row = ROW_NO_1)

        #  According to the position, update the count number
        if currentPosition != previousPosition:
            if currentPosition == POSITION_LEFT or POSITION_LEFT == POSITION_RIGHT:
                if cycleIndexPos == currentPosition:
                    cycleCounter += 1
                elif currentPosition == POSITION_MIDDLE:
                    if cycleIndexPosMiddle and (cycleIndexPos == currentPosition):
                        cycleCounter += 1
                    cycleIndexPosMiddle = not cycleIndexPosMiddle
                else:
                    pass

        # Update the count in the LCD
        previousPosition = currentPosition
        printCount(row = ROW_NO_2, count = cycleCounter)

        # If reach the full count number then turn on the Finish LED
        if cycleCounter >= 7500000:
            gpio.digitalWrite(ON_BOARD_LED_PIN, HIGH)
            cycleCounter = 0

        # Reset button debounce logic
        ResetBtnReading = gpio.digitalRead(RESET_PUSH_SWITCH_PIN)

        if ResetBtnReading != lastButtonState:
            lastDebounceTime = time.time()

        if ((time.time() - lastDebounceTime) * 1000) > debounceDelay:
            if ResetBtnReading != buttonState:
                buttonState = ResetBtnReading

                if buttonState == LOW:
                    lcd.write("Count Reseting...   ", row = ROW_NO_3)
                    ResetTrigger = True

        lastButtonState = ResetBtnReading

        # If reset button pressed then clean the old stuffs
        if ResetTrigger:
            cycleCounter = 0
            setCycleCount(cycleCounter)
            ResetTrigger = False
            time.sleep(2)
            lcd.write(" "*LCD_MODULE_NO_OF_COLUMN, row = ROW_NO_3)


# Entry point main function
def main():
    setup()
    loop()


if __name__ == "__main__":
    main()
