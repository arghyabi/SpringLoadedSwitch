import os

SCRIPT_PATH             = os.path.dirname(os.path.abspath(__file__))
BASE_PATH               = os.path.dirname(SCRIPT_PATH)

CONFIG_YAML_FILE        = os.path.join(BASE_PATH, "config.yaml")
RT_DB_FILE              = os.path.join(BASE_PATH, "rtDb.json")

INPUT                   = 0
OUTPUT                  = 1

PULL_UP                 = 0
PULL_DOWN               = 1

HIGH                    = 1
LOW                     = 0

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
