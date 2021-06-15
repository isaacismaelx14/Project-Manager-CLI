import json

_FILE_NAME = 'PManager.json'

def _create(data):
    with open(_FILE_NAME, 'w') as file:
        json.dump(data, file, indent=2)

def start(data):
    _create(data)

