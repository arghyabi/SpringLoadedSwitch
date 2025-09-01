from utility import *
from doubleSwitch import *
from singleSwitch import *
from common import *


def app_setup(switchModel):
    if switchModel == SWITCH_MODEL_DOUBLE:
        doubleSwitchSetup(switchModel)
    elif switchModel == SWITCH_MODEL_SINGLE:
        singleSwitchSetup(switchModel)
    else:
        print("Unknown switch model. Exiting.")
        exit(1)


def app_loop(switchModel):
    if switchModel == SWITCH_MODEL_DOUBLE:
        rtn = doubleSwitchLoop(switchModel)
    elif switchModel == SWITCH_MODEL_SINGLE:
        rtn = singleSwitchLoop(switchModel)
    else:
        print("Unknown switch model. Exiting.")
        rtn = LOOP_RTN_TYPE_ERROR

    return rtn


# Entry point main function
def main():
    print("Starting Spring Loaded Switch application.")
    createRtDbFile()
    print("Database creation done!")
    print("Getting Switch Model...")
    switchModel = getSwitchModel()
    # switchModel = SWITCH_MODEL_DOUBLE
    # switchModel = SWITCH_MODEL_SINGLE
    print(f"Detected Switch Model: {switchModel}")
    print("Entering initial setup.")
    app_setup(switchModel)
    print("Entering main loop.")
    rtn = app_loop(switchModel)
    print(f"Main loop returned: {rtn}")
    if rtn == LOOP_RTN_TYPE_SW_CHANGE:
        print("Switch model change detected. Restarting application...")
        main()
    else:
        print("Exiting application.")
        exit(-1)


if __name__ == "__main__":
    main()
