import os

SCRIPT_PATH             = os.path.dirname(os.path.abspath(__file__))
BASE_PATH               = os.path.dirname(SCRIPT_PATH)

CONFIG_YAML_FILE        = os.path.join(BASE_PATH, "config.yaml")
RT_DB_FILE              = os.path.join(BASE_PATH, "rtDb.json")

INPUT                   = False
OUTPUT                  = True

PULL_UP                 = False
PULL_DOWN               = True

HIGH                    = True
LOW                     = False

LCD_MODULE_NO_OF_ROW    = 4
LCD_MODULE_NO_OF_COLUMN = 20

POSITION_LEFT           = -1
POSITION_MIDDLE         = 0
POSITION_RIGHT          = 1

ROW_NO_0                = 0
ROW_NO_1                = 1
ROW_NO_2                = 2
ROW_NO_3                = 3

WEBSITE_FOLDER          = "Web"

CONFIG_UPDATE_AVAILABLE = True
NO_CONFIG_UPDATE        = False

SWITCH_MODEL_DOUBLE     = "Type-D"
SWITCH_MODEL_SINGLE     = "Type-S"

LOOP_RTN_TYPE_ERROR     = "error"
LOOP_RTN_TYPE_SW_CHANGE = "switch"

