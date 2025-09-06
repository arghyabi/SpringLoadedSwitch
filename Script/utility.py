import os
import yaml
import json

from common import *


def getYamlData(yamlFile):
    if not os.path.exists(yamlFile):
        raise Exception(f"ERROR: {yamlFile} File not Found!!")

    try:
        with open(yamlFile) as file:
            config = yaml.load(file, Loader = yaml.FullLoader)
            return config
    except Exception as e:
        print(f"Not able to read {yamlFile} file")


def setYamlData(yamlFile, data):
    try:
        with open(yamlFile, "w") as file:
            json.dump(data, file, indent = 4)
    except Exception as e:
        print(f"Not able to create {yamlFile}!!!")


def getAppVersion():
    configData = getYamlData(CONFIG_YAML_FILE)
    if configData:
        return configData.get("appVersion")
    else:
        return "0.0.0.0000"


def createRtDbFile(ForceDbCreation = False):
    if not os.path.exists(RT_DB_FILE) or ForceDbCreation:
        blankData = {
            "cycleCount": 0,
            "switchModel": SWT_MODEL_DOUBLE_TYPE_B,
            "motorStatus": 1
        }

        setYamlData(RT_DB_FILE, blankData)
    else:
        configData = getYamlData(RT_DB_FILE)
        if configData == None or configData == "":
            print(f"Config data : '{configData}'")
            print(f"Re-creating database..")
            os.remove(RT_DB_FILE)
            createRtDbFile()



def getCycleCount():
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        cycleCount = rtData.get("cycleCount")
        if cycleCount == None:
            cycleCount = 0

        return int(cycleCount)
    else:
        return 0


def getTotalCount():
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        totalCount = rtData.get("maxCount")
        if totalCount == None:
            configData = getYamlData(CONFIG_YAML_FILE)
            if configData:
                totalCount = configData.get("maxCount")

            if totalCount == None:
                totalCount = 0

        return int(totalCount)
    return 0


def setCycleCount(count: int):
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        rtData["cycleCount"] = count
        setYamlData(RT_DB_FILE, rtData)


def getConfigUpdateStatus():
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        updateNeeded = rtData.get("updateNeeded")
        if updateNeeded == None:
            updateNeeded = NO_CONFIG_UPDATE

        return int(updateNeeded)
    return 0


def setConfigUpdateStatus(status):
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        rtData["updateNeeded"] = status
        setYamlData(RT_DB_FILE, rtData)


def getSwitchModel():
    switchModel = SWT_MODEL_DOUBLE_TYPE_B
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        switchModel = rtData.get("switchModel")
        if switchModel == None:
            switchModel = SWT_MODEL_DOUBLE_TYPE_B

    return switchModel


def setSwitchModel(switchModel):
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        rtData["switchModel"] = switchModel
        setYamlData(RT_DB_FILE, rtData)


def getMotorControlStatus():
    motorStatus = LOW
    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        motorStatus = rtData.get("motorStatus")
        if motorStatus == None:
            motorStatus = LOW

    return motorStatus


def setMotorControlStatus(status):
    status = 1 if status == HIGH else 0

    rtData = getYamlData(RT_DB_FILE)
    if rtData:
        rtData["motorStatus"] = status
        setYamlData(RT_DB_FILE, rtData)
