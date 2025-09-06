from common       import *
from utility      import *
from doubleSwitch import *
from singleSwitch import *


def app_setup(switchModel):
    if switchModel == SWT_MODEL_DOUBLE_TYPE_B or switchModel == SWT_MODEL_DOUBLE_TYPE_C or switchModel == SWT_MODEL_DOUBLE_TYPE_E:
        doubleSwitchSetup(switchModel)
    elif switchModel == SWT_MODEL_SINGLE_TYPE_A or switchModel == SWT_MODEL_SINGLE_TYPE_D:
        singleSwitchSetup(switchModel)
    else:
        print("Unknown switch model. Exiting.")
        exit(1)


def app_loop(switchModel):
    if switchModel == SWT_MODEL_DOUBLE_TYPE_B or switchModel == SWT_MODEL_DOUBLE_TYPE_C or switchModel == SWT_MODEL_DOUBLE_TYPE_E:
        rtn, model = doubleSwitchLoop(switchModel)
    elif switchModel == SWT_MODEL_SINGLE_TYPE_A or switchModel == SWT_MODEL_SINGLE_TYPE_D:
        rtn, model = singleSwitchLoop(switchModel)
    else:
        print("Unknown switch model. Exiting.")
        rtn = LOOP_RTN_TYPE_ERROR
        model = None

    return rtn, model


# Entry point main function
def main(ForceDbCreation = False, newSwModel = None):
    print(f"Starting Spring Loaded Switch application. {getAppVersion()}")
    createRtDbFile(ForceDbCreation)
    print("Database creation done!")
    if newSwModel:
        print("Updating new Switch Model...")
        setSwitchModel(newSwModel)
    print("Getting Switch Model...")
    switchModel = getSwitchModel()
    print(f"Detected Switch Model: {switchModel}")
    print("Entering initial setup.")
    app_setup(switchModel)
    print("Entering main loop.")
    rtn, model = app_loop(switchModel)
    print(f"Main loop returned: {rtn}")
    if rtn == LOOP_RTN_TYPE_SW_CHANGE:
        print("Switch model change detected. Restarting application...")
        main(ForceDbCreation = True, newSwModel = model)
    else:
        print("Exiting application.")
        exit(-1)


if __name__ == "__main__":
    main()
