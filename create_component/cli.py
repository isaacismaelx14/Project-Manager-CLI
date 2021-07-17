import argparse

from pathlib import Path


def start() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='Project Files Manager',
        description='A program to manage your project files'
    )
    parser.add_argument(
        'component',
        nargs='?',
        default=None,
        help='The name of the files'
    )
    parser.add_argument(
        '-d', '--destination',
        default=None,
        type=Path,
        help='Directory where going to build files',
    )
    parser.add_argument(
        '-c', '--config',
        action='store_true',
        help='Create file PManager.json'
    )
    parser.add_argument(
        '--no-style',
        action='store_true',
        help='Ignore the style file'
    )
    parser.add_argument(
        '--no-test',
        action='store_true',
        help='Ignore the test file'
    )
    parser.add_argument(
        '--no-index',
        action='store_true',
        help='Ignore the index file'
    )

    return parser.parse_args()
