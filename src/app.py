import argparse
import os
import time
import options
import create_files as filesController

from pathlib import Path
from sys import stderr
from colors import red, green, blue, yellow
from controllers import clearConsole
from errorManager import ErrorExp


def run_opts():
    time.sleep(1)
    return options.start()


def create_component_folder(filePath: Path, fn):
    if(filePath.exists() == False):
        os.mkdir(filePath)
        print(f'{blue(f"{fn} folder")} {green("created")}')


def create_files(dest: Path, fn: str, opt):
    select_type = opt['style_type']
    ft = opt['ft']
    ftc = opt['ftc']
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
        opt = run_opts()
        create_files(dest.absolute(), fn, opt)
    elif dest.is_file():
        raise ErrorExp(red(f'{dest} is not a directory'))
    else:
        no_exist_directory(dest)


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Project Files Manager',
        description='A program to manage your project files'
    )
    parser.add_argument(
        'component',
        help='The name of the files'
    )
    parser.add_argument(
        '-d', '--destination',
        default=Path('src', 'components'),
        type=Path,
        help='Directory where going to build files',
    )

    return parser.parse_args()


def main():
    args = cli()
    clearConsole()
    try:
        get_directory(args.destination, args.component)

    except ErrorExp as e:
        print(e, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
