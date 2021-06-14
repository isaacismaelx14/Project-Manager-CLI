import argparse

from pathlib import Path


def start() -> argparse.Namespace:
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
        default=None,
        type=Path,
        help='Directory where going to build files',
    )
    parser.add_argument(
        '-tc', '--temporal-config',
        action='store_true',
        help='Define if you want to use the PManager.json',
    )

    return parser.parse_args()
