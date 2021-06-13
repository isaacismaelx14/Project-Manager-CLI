import json
from pathlib import Path

_FILE_NAME = 'PManager.json'
_PATH = Path(_FILE_NAME)


def read_file():
    file_json_config = open(_PATH)
    config = json.load(file_json_config)
    return config


def exist_config_file():
    if(_PATH.is_file()):
        return True
    return False


def start():
    if(exist_config_file()):
        return read_file()
    else:
        return False


start()
