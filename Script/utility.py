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
    return configData.get("appVersion")


def createRtDbFile():
    if not os.path.exists(RT_DB_FILE):
        blankData = {
            "cycleCount": 0
        }

        setYamlData(RT_DB_FILE, blankData)


def getCycleCount():
    rtData = getYamlData(RT_DB_FILE)
    cycleCount = rtData.get("cycleCount")
    if cycleCount == None:
        cycleCount = 0

    return int(cycleCount)


def getTotalCount():
    rtData = getYamlData(RT_DB_FILE)
    totalCount = rtData.get("maxCount")
    if totalCount == None:
        configData = getYamlData(CONFIG_YAML_FILE)
        totalCount = configData.get("maxCount")

    if totalCount == None:
        totalCount = 0

    return int(totalCount)


def setCycleCount(count: int):
    rtData = getYamlData(RT_DB_FILE)
    rtData["cycleCount"] = count
    setYamlData(RT_DB_FILE, rtData)


def getConfigUpdateStatus():
    rtData = getYamlData(RT_DB_FILE)
    updateNeeded = rtData.get("updateNeeded")
    if updateNeeded == None:
        updateNeeded = NO_CONFIG_UPDATE

    return int(updateNeeded)


def setConfigUpdateStatus(status):
    rtData = getYamlData(RT_DB_FILE)
    rtData["updateNeeded"] = status
    setYamlData(RT_DB_FILE, rtData)
