
import os
import time
import functions.options
import json
import functions.cli as cli
import functions.create_files as filesController
import functions.options as options
import config.create as create_config

from pathlib import Path
from sys import stderr
from functions.colors import red, green, blue, yellow
from functions.controllers import clearConsole
from functions.errorManager import ErrorExp
from config import read as read_cofig


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


def create_component_folder(filePath: Path, fn):
    if(filePath.exists() == False):
        os.mkdir(filePath)
        print(f'{blue(f"{fn} folder")} {green("created")}')


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
        filesController.create_test_js(fileAbsoulte, fn, ft, use_index)


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


def create_directory(dir: Path):
    os.makedirs(dir, exist_ok=True)
    main()


def no_exist_directory(dir: Path):
    message = f"{yellow(f'{dir}')} don\'t exist, {blue('do you want to create?')}"
    resp = accept(message)

    if(resp == "True"):
        create_directory(dir.absolute())
    elif(resp == "False"):
        print('please execute the CLI again and enter another directory')
        exit()
    else:
        no_exist_directory(dir)


def get_directory(dest: Path, fn: str):
    if dest.is_dir():
        create_files(dest.absolute(), fn, _COMPONENT_CONFIG)
    elif dest.is_file():
        raise ErrorExp(red(f'{dest} is not a directory'))
    else:
        no_exist_directory(dest)


def set_config(config):
    main_keys = ['dir', 'lang']
    for key in main_keys:
        if key in config:
            _CONFIG[key] = config[key]


def _compoents_warnings(component_config):
    if(component_config['component_file_type'] == 'jsx' and component_config['lang'] == 'ts'):
        print(yellow(
            'warning:'), 'Your filetype is .ts and your components .jsx (config file)')
        press_e_to_exit_and_c_to_continue()
    if(component_config['component_file_type'] == 'tsx' and component_config['lang'] == 'js'):
        print(yellow('warning:'), 'Your filetype is .js and your components .tsx (config file)')
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
    res = input(f"Press {red('[x]')} to exit and {green('[c]')} to continue: ").lower()
    if(res == 'c'):
        pass
    elif(res == 'x'):
        exit(2)
    else:
        raise ErrorExp(red(f'"{res}" is not a valid value'))


def get_config():
    config = read_cofig.start()

    if(config):
        set_config(config)
        set_component_config(config)


def get_data_config():
    return {
        'dest': Path(_CONFIG['dir'])
    }

def local_cli():
    print(f"{blue('Project Manager')} {green('CLI')}")
    print(f"Selecte an option:")
    print("\n")
    print("""
************************************************
******     [1] Create component          *******
******     [2] Create config file       *******
************************************************
        """)
    valut = input('Select a value (default 1): ')


def main_task(component,arg_dest):
    get_config()
    config = get_data_config()
    dest = arg_dest if arg_dest else config['dest']
    clearConsole()
    get_directory(dest, component)

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
            local_cli()
    except ErrorExp as e:
        clearConsole()
        print(e, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
