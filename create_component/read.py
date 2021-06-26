# start
import json
from pathlib import Path
from sys import stderr
from .colors import red

_FILE_NAME = 'PManager.json'
_PATH = Path(_FILE_NAME)

num: int = 0


class ErrorExp(Exception):
    pass


def check_config(config):
    errors = []
    final_errors = []
    if('dir' in config):
        errors.append(check_dir(config['dir']))
    if('lang' in config):
        errors.append(check_lang(config['lang']))
    if('component' in config):
        comp = config['component']
        errors.extend(check_componet(comp))

    for err in errors:
        if(err != None):
            final_errors.append(err)
    def add_s():
        if(len(final_errors) > 1):
            return 's'
        return ''

    if(len(final_errors) > 0):
        raise ErrorExp(f'{red(f"error{add_s()}:")} \n \t' + '\n \t'.join(final_errors))


def check_dir(dir):
    if(type(dir) != str):
        return('dir must be an string (config file)')


def check_lang(lang):
    if(type(lang) != str):
        return('lang must be an string (config file)')


def check_type(types, check, suffix):
    num = 0
    length = len(types)
    for _type in types:
        num = num + 1  # detect the N times that exec this code
        if(_type == check):
            break
        elif(length == num):
            return(f'{check} is invalid in {suffix} (config file)')


def check_componet(comp):
    lang_types = ['js', 'ts']
    component_file_types = ['jsx', 'tsx', 'js']
    style_type_types = ['none', 'css', 'scss', 'sass']

    errors = []

    if type(comp) != dict:
        errors.append('component must be an object (config file)')
    # Lang
    if('lang' in comp):
        if type(comp['lang']) != str:
            errors.append(
                'component -> lang must be an js or ts (config file)')
        errors.append(check_type(
            lang_types, comp['lang'], 'component -> lang'))

    # Component file type
    if('component_file_type' in comp):
        if(type(comp['component_file_type']) != str):
            errors.append(
                'component_file_type be an object (config file)')
        errors.append(check_type(component_file_types, comp['component_file_type'], 'component_file_type'))
    # Style type
    if('style_type' in comp):
        if(type(comp['style_type']) != str):
            errors.append(
                'style_type must be an none, css, scss, or sass (config file)')
        errors.append(check_type(style_type_types, comp['style_type'], 'style_type'))
    # use test
    if('use_test' in comp and type(comp['use_test']) != bool):
        errors.append('use_test must be an true or false (config file)')
    # use folder
    if('use_folder' in comp and type(comp['use_folder']) != bool):
        errors.append('use_folder must be an true or false (config file)')
    # use index
    if('use_index' in comp and type(comp['use_index']) != bool):
        errors.append('use_index must be an true or false (config file)')

    return errors


def read_file():
    file_json_config = open(_PATH)
    try:
        config = json.load(file_json_config)
        return config
    except:
        return None


def exist_config_file():
    if(_PATH.is_file()):
        return True
    return False


def start():
    if(exist_config_file()):
        try:
            obj = read_file()
            check_config(obj)
            return obj
        except ErrorExp as e:
            print(e, file=stderr)
            exit(1)
    else:
        return False

# Test
# print(json.dumps(start(), indent=3))
