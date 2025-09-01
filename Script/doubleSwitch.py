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
TotalCounter  = 0

previousPosition = None
currentPosition  = None

ResetBtnReading  = None
buttonState      = None

ResetTrigger     = False
isConfigReadNeed = True
cycleIndexPosMiddle = False

lastButtonState  = HIGH
debounceDelay    = 5000
lastDebounceTime = 0


# Introduction banner print
def startIntroPrint():
    lcd.write("SPRING LOADED", row = ROW_NO_0, center = True)
    lcd.write("SWITCH TESTER", row = ROW_NO_1, center = True)
    appVersion = getAppVersion()
    print(f"Application version: {appVersion}")
    lcd.write(f"Version: {appVersion}", row = ROW_NO_3, padding = True)
    time.sleep(3)
    lcd.clean()
    time.sleep(0.5)
    lcd.turnOffBacklight()
    time.sleep(1)
    lcd.turnOnBacklight()
    time.sleep(1)


# This is the gpio initialization
def gpioInitialization():
    gpio.pinMode(ON_BOARD_LED_PIN, OUTPUT)
    gpio.pinMode(GPIO_3V3_1_PIN, OUTPUT)
    gpio.pinMode(GPIO_3V3_2_PIN, OUTPUT)

    gpio.pinMode(MICRO_SWITCH_S1_NC_PIN, INPUT, PULL_DOWN)
    gpio.pinMode(MICRO_SWITCH_S1_NO_PIN, INPUT, PULL_DOWN)
    gpio.pinMode(MICRO_SWITCH_S2_NC_PIN, INPUT, PULL_DOWN)
    gpio.pinMode(MICRO_SWITCH_S2_NO_PIN, INPUT, PULL_DOWN)

    gpio.pinMode(POSITION_RIGHT_LED_PIN, OUTPUT)
    gpio.pinMode(POSITION_MIDDLE_LED_PIN, OUTPUT)
    gpio.pinMode(POSITION_LEFT_LED_PIN, OUTPUT)

    gpio.pinMode(MOTOR_ON_OFF_PIN, OUTPUT)

    gpio.pinMode(RESET_PUSH_SWITCH_PIN, INPUT)

    gpio.digitalWrite(GPIO_3V3_1_PIN, HIGH)
    gpio.digitalWrite(GPIO_3V3_2_PIN, HIGH)

    gpio.digitalWrite(POSITION_RIGHT_LED_PIN, LOW)
    gpio.digitalWrite(POSITION_MIDDLE_LED_PIN, LOW)
    gpio.digitalWrite(POSITION_LEFT_LED_PIN, LOW)

    gpio.digitalWrite(MOTOR_ON_OFF_PIN, LOW)


# Time print function
def printCurrentTime(row: int):
    lcd.write(datetime.now().strftime('%I:%M:%S %p %d/%m/%y'), row = row, padding = True)
    # time.sleep(0.1)


# Print the count value
def printCountValue(row: int, currentCount: int, totalCount: int):
    lcd.write(f"Test:{currentCount}/{totalCount}", row = row, padding = True)


# Turn on only the position LED
def showPositionLED(position: int|None):
    if position == POSITION_LEFT:
        gpio.digitalWrite(POSITION_RIGHT_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_MIDDLE_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_LEFT_LED_PIN, HIGH)

    elif position == POSITION_RIGHT:
        gpio.digitalWrite(POSITION_RIGHT_LED_PIN, HIGH)
        gpio.digitalWrite(POSITION_MIDDLE_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_LEFT_LED_PIN, LOW)

    elif position == POSITION_MIDDLE:
        gpio.digitalWrite(POSITION_RIGHT_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_MIDDLE_LED_PIN, HIGH)
        gpio.digitalWrite(POSITION_LEFT_LED_PIN, LOW)

    else:
        gpio.digitalWrite(POSITION_RIGHT_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_MIDDLE_LED_PIN, LOW)
        gpio.digitalWrite(POSITION_LEFT_LED_PIN, LOW)


#  This is the void Setup() function just like Arduino code
def doubleSwitchSetup(model: str):
    global cycleIndexPos
    global previousPosition
    global cycleCounter
    global TotalCounter

    startIntroPrint()
    print("Intro print done!")
    gpioInitialization()
    print("GPIO initialization done!")

    lcd.write(f"Model: {model}", row = ROW_NO_1, center = True)

    #################################################
    ##         S1_NO     S1_NC     S2_NO    S2_NC  ##
    ## LEFT      0         1         1       0     ##
    ## MID       1         0         1       0     ##
    ## RIGHT     1         0         0       1     ##
    #################################################

    if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
        previousPosition = POSITION_LEFT
        cycleIndexPos    = POSITION_LEFT
        print("Initial position: LEFT")

    if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
        previousPosition = POSITION_MIDDLE
        cycleIndexPos    = POSITION_MIDDLE
        print("Initial position: MIDDLE")

    if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
        previousPosition = POSITION_RIGHT
        cycleIndexPos    = POSITION_RIGHT
        print("Initial position: RIGHT")

    ########## TEST BEGIN ###############
    if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and  gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN) and\
        gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN) and\
        gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
        previousPosition = POSITION_MIDDLE
        cycleIndexPos    = POSITION_MIDDLE
        print("Probably No switch found; All pin are HIGH ... !!")

    if previousPosition == None and cycleIndexPos == None:
        raise Exception("Someting Wrong!! Not able to read switch posiiton!!")

    ########## TEST END## ###############

    cycleCounter = getCycleCount()
    TotalCounter = getTotalCount()
    print(f"Current Counter: {cycleCounter}")
    print(f"Max Counter    : {TotalCounter}")
    printCountValue(row = ROW_NO_3, currentCount = cycleCounter, totalCount = TotalCounter)
    setCycleCount(cycleCounter)

    gpio.digitalWrite(ON_BOARD_LED_PIN, LOW)


# This is the void loop() function just like Arduino code
def doubleSwitchLoop(model: str):
    global isConfigReadNeed
    global previousPosition
    global cycleIndexPos
    global currentPosition
    global cycleCounter
    global TotalCounter
    global cycleIndexPosMiddle
    global ResetBtnReading
    global lastButtonState
    global debounceDelay
    global buttonState
    global ResetTrigger
    global lastDebounceTime

    rtn = LOOP_RTN_TYPE_ERROR

    while True:
        gpio.digitalWrite(MOTOR_ON_OFF_PIN, HIGH)
        setMotorControlStatus(HIGH)
        printCurrentTime(ROW_NO_0)

        #################################################
        ##         S1_NO     S1_NC     S2_NO    S2_NC  ##
        ## LEFT      0         1         1       0     ##
        ## MID       1         0         1       0     ##
        ## RIGHT     1         0         0       1     ##
        #################################################

        # Reading the gpio pin for the switchs
        if gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
            currentPosition = POSITION_LEFT
            lcd.write("Position Left  ", row = ROW_NO_2)
            print("Position Left")

        if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN):
            currentPosition = POSITION_MIDDLE
            lcd.write("Position Middle", row = ROW_NO_2)
            print("Position Middle")

        if gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN) and gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN):
            currentPosition = POSITION_RIGHT
            lcd.write("Position Right ", row = ROW_NO_2)
            print("Position Right")

        print("S1_NO:", gpio.digitalRead(MICRO_SWITCH_S1_NO_PIN), end="\t")
        print("S1_NC:", gpio.digitalRead(MICRO_SWITCH_S1_NC_PIN), end="\t")
        print("S2_NO:", gpio.digitalRead(MICRO_SWITCH_S2_NO_PIN), end="\t")
        print("S2_NC:", gpio.digitalRead(MICRO_SWITCH_S2_NC_PIN))

        # Turn on the postion LED
        showPositionLED(currentPosition)

        #  According to the position, update the count number
        countUpdate = False
        if currentPosition != previousPosition:
            if currentPosition == POSITION_LEFT or currentPosition == POSITION_RIGHT:
                if cycleIndexPos == currentPosition:
                    cycleCounter += 1
                    countUpdate = True
            elif currentPosition == POSITION_MIDDLE:
                if cycleIndexPosMiddle and (cycleIndexPos == currentPosition):
                    cycleCounter += 1
                    countUpdate = True
                cycleIndexPosMiddle = not cycleIndexPosMiddle
            else:
                pass

        previousPosition = currentPosition

        # update current and total count value if config update avaialabe
        if getConfigUpdateStatus() == CONFIG_UPDATE_AVAILABLE:
            cycleCounter = getCycleCount()
            TotalCounter = getTotalCount()
            motorStatus  = getMotorControlStatus()
            switchModel  = getSwitchModel()
            setConfigUpdateStatus(NO_CONFIG_UPDATE)
            printCountValue(row = ROW_NO_3, currentCount = cycleCounter, totalCount = TotalCounter)
            gpio.digitalWrite(MOTOR_ON_OFF_PIN, motorStatus)
            if switchModel != model:
                rtn = LOOP_RTN_TYPE_SW_CHANGE
                break

        # Update the count in the LCD
        if countUpdate:
            printCountValue(row = ROW_NO_3, currentCount = cycleCounter, totalCount = TotalCounter)
            setCycleCount(cycleCounter)
            countUpdate = False

        # If reach the full count number then turn on the Finish LED
        if cycleCounter >= TotalCounter:
            gpio.digitalWrite(ON_BOARD_LED_PIN, HIGH)
            gpio.digitalWrite(MOTOR_ON_OFF_PIN, LOW)
            setMotorControlStatus(LOW)
            lcd.write("Count Finished!", row = ROW_NO_3, padding = True)
            print("Count Finished!")
            cycleCounter = 0

        # Reset button debounce logic
        ResetBtnReading = gpio.digitalRead(RESET_PUSH_SWITCH_PIN)

        if ResetBtnReading != lastButtonState:
            lastDebounceTime = time.time()

        if ((time.time() - lastDebounceTime) * 1000) > debounceDelay:
            if ResetBtnReading != buttonState:
                buttonState = ResetBtnReading

                if buttonState == LOW:
                    lcd.write("Count Reseting...", row = ROW_NO_3, padding = True)
                    ResetTrigger = True

        lastButtonState = ResetBtnReading

        # If reset button pressed then clean the old stuffs
        if ResetTrigger:
            gpio.digitalWrite(MOTOR_ON_OFF_PIN, LOW)
            setMotorControlStatus(LOW)
            cycleCounter = 0
            gpio.digitalWrite(ON_BOARD_LED_PIN, LOW)
            setCycleCount(cycleCounter)
            ResetTrigger = False
            time.sleep(2)
            lcd.write(" "*LCD_MODULE_NO_OF_COLUMN, row = ROW_NO_3)
            time.sleep(1)
            printCountValue(row = ROW_NO_3, currentCount = cycleCounter, totalCount = TotalCounter)

    # Return the loop status
    return rtn

# Entry point main function
def main():
    print("Entering initial setup.")
    doubleSwitchSetup(SWITCH_MODEL_DOUBLE)
    print("Entering main loop.")
    doubleSwitchLoop(SWITCH_MODEL_DOUBLE)


if __name__ == "__main__":
    main()
