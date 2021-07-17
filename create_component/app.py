
import os
import time
import json
from pathlib import Path
from sys import stderr

from . import cli as cli
from . import create_files as filesController
from . import options as options
from . import create as create_config
from . import read as read_cofig

from .colors import red, green, blue, yellow
from .controllers import clearConsole
from .errorManager import ErrorExp


_COMPONENT_CONFIG = {
    "lang": 'js',
    "component_file_type": 'jsx',
    "style_type": 'css',
    "use_test": True,
    "use_folder": True,
    "use_index": True
}

_CONFIG = {
    "dir": 'src/components/',
    "lang": None,
    "component": _COMPONENT_CONFIG
}

_DESTINATION = None
_FILE_NAME = None

class Exit(Exception):
    pass

# Create a folder for a the components
def create_component_folder(filePath: Path, fn):
    if(filePath.exists() == False):
        os.mkdir(filePath)
        print(f'{blue(f"{fn} folder")} {green("created")}')

# Create the files of the component
def create_files(dest: Path, fn: str, opt):
    select_type = opt['style_type']
    ft = opt['lang']
    ftc = opt['component_file_type']
    use_test = opt['use_test']
    use_index = opt['use_index']
    use_folder = opt['use_folder']

    clearConsole()
    print("creating...")

    filePath = dest
    if(use_folder):
        filePath = Path(dest, fn)
        create_component_folder(filePath, fn)

    fileAbsoulte = Path(filePath, fn)

    filesController.create_jsx(fileAbsoulte, fn, select_type, ftc)
    if use_index:
        filesController.create_index(filePath, fn, ft)
    if(select_type != 'none'):
        filesController.create_style(filePath, fn, select_type)
    if use_test:
        filesController.create_test_js(fileAbsoulte, fn, ft, ftc,use_index)

#   Print a message with option (Yes or No) and return the answer in str
#   if you press a valid as Y, Yes, N or No, this functin return "True"
#   or "False". But if you type a not valid value return "Invalid"
def accept(message: str) -> str:
    response = input(
        f'{message} {green("(yes/no)")}: ').lower()
    if(response == 'yes' or response == 'y'):
        return "True"
    elif(response == 'no' or response == 'n'):
        return "False"
    else:
        print(f'"{response}" is not supported, please try again...')
        return "Invalid"

# Create a directory and  go to directory and recive a funtion
# to now were comeback when finish
def create_directory(dir: Path, callback):
    os.makedirs(dir, exist_ok=True)
    callback()

# Print a message asking if you want to create a directory
def no_exist_directory():
    dir = _DESTINATION
    message = f"{yellow(f'{dir}')} don\'t exist, {blue('do you want to create?')}"
    resp = accept(message)

    if(resp == "True"):
        create_directory(dir.absolute(), get_directory)
    elif(resp == "False"):
        print('please execute the CLI again and enter another directory')
        Exit(0)
    else:
        no_exist_directory(dir)

# detect if is a directory or no and if the directory exists
def get_directory():
    dest = Path(_DESTINATION)
    fn = _FILE_NAME
    if dest.is_dir():
        create_files(dest.absolute(), fn, _COMPONENT_CONFIG)
    elif dest.is_file() or dest.is_socket():
        raise ErrorExp(red(f'{dest} is not a directory'))
    else:
        no_exist_directory()

# set the cofiguration from the config file 
def set_config(config):
    main_keys = ['dir', 'lang']
    for key in main_keys:
        if key in config:
            _CONFIG[key] = config[key]

# Print warnings while set the components config
def _compoents_warnings(component_config):
    if(component_config['component_file_type'] == 'jsx' and component_config['lang'] == 'ts'):
        print(yellow(
            'warning:'), 'Your filetype is .ts and your components .jsx (config file)')
        press_e_to_exit_and_c_to_continue()
    if(component_config['component_file_type'] == 'tsx' and component_config['lang'] == 'js'):
        print(yellow('warning:'),
            'Your filetype is .js and your components .tsx (config file)')
        press_e_to_exit_and_c_to_continue()


def set_component_config(config):
    keys = ['lang', 'component_file_type', 'style_type',
            'use_test', 'use_folder', 'use_index']
    if 'component' in config:
        component_config = config['component']
        for key in keys:
            if key in component_config:
                _COMPONENT_CONFIG[key] = component_config[key]
            if key == 'component_file_type':
                if('lang' in component_config):
                    if component_config['lang'] == 'ts':
                        _COMPONENT_CONFIG[key] = 'tsx'
                    if('component_file_type' in component_config):
                        _compoents_warnings(component_config)
                else:
                    if component_config['component_file_type'] == 'tsx':
                        _COMPONENT_CONFIG['lang'] = 'ts'


def press_e_to_exit_and_c_to_continue():
    res = input(
        f"Press {red('[x]')} to exit and {green('[c]')} to continue: ").lower()
    if(res == 'c'):
        pass
    elif(res == 'x'):
        exit(2)
    else:
        raise ErrorExp(red(f'"{res}" is not a valid value'))

#Get data from config file
def get_config():
    config = read_cofig.start()

    if(config):
        set_config(config)
        set_component_config(config)


def get_data_config():
    return {
        'dest': Path(_CONFIG['dir'])
    }

# detect if a string is empty
def is_empty(string: str)-> bool:
    new_str = string.strip()
    if(len(new_str) == 0):
        return True
    return False


def create_component():
    component = input('Type the name of the component: ')
    main_task(component)


def get_selection_cli(selection):
    clearConsole()
    if(is_empty(selection)):
        print('[Default]')
        selection = '1'
    if(selection == "1"):
        print(green('Create component'))
        print('\n')
        create_component()
    elif(selection == "2"):
        create_config.start(options.start())
    elif(selection == 'q'):
        Exit(0)


def local_cli()->str:
    print(f"{blue('Project Manager')} {green('CLI')}")
    print(f"Selecte an option:")
    print(f"""
{yellow('******************************************************')}
{yellow('******')}           {red('[1]')} {blue('Create component')}          {yellow('*******')}
{yellow('******')}           {red('[2]')} {blue('Create config file')}        {yellow('*******')}
{yellow('******')}           {red('[q]')} {blue('Exit')}                      {yellow('*******')}
{yellow('******************************************************')}
        """)
    return input(f'Select a value {red("(default 1)")}: ').lower()


def main_task(component, arg_dest=None):
    global _DESTINATION
    global _FILE_NAME
    get_config()
    config = get_data_config()
    dest = arg_dest if arg_dest else config['dest']
    clearConsole()
    _DESTINATION = dest
    _FILE_NAME = component
    get_directory()


def main():
    clearConsole()
    try:
        args = cli.start()
        component = args.component
        arg_dest = args.destination
        arg_config = args.config
        if(component):
            main_task(component, arg_dest)
        elif(component == None and arg_config):
            create_config.start(options.start())
        else:
            get_selection_cli(local_cli())
    except ErrorExp as e:
        clearConsole()
        print(e, file=stderr)
        exit(1)
    except KeyboardInterrupt:
        clearConsole()
    except Exit as code:
        clearConsole()
        exit(code)


if __name__ == '__main__':
    main()
