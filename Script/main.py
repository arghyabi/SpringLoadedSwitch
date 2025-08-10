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
        doubleSwitchLoop()
    elif switchModel == SWITCH_MODEL_SINGLE:
        singleSwitchLoop()
    else:
        print("Unknown switch model. Exiting.")
        exit(1)


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
    app_loop(switchModel)


if __name__ == "__main__":
    main()
