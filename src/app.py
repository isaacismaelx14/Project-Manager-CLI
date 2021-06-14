
import os
import time
import functions.options
import json
import functions.cli as cli
import functions.create_files as filesController


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
                        if(component_config['component_file_type'] == 'jsx' and component_config['lang'] == 'ts'):
                                print(yellow('warning:'), 'Your filetype is .ts and your components .jsx (config file)')
                                press_e_to_exit_and_c_to_continue()
                        if(component_config['component_file_type'] == 'tsx' and component_config['lang'] == 'js'):
                                print(yellow('warning:'), 'Your filetype is .js and your components .tsx (config file)')
                                press_e_to_exit_and_c_to_continue()
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


def main():
    clearConsole()
    try:
        get_config()
        args = cli.start()
        arg_dest = args.destination
        config = get_data_config()

        dest = arg_dest if arg_dest else config['dest']

        component = args.component
        clearConsole()
        get_directory(dest, component)
    except ErrorExp as e:
        clearConsole()
        print(e, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
