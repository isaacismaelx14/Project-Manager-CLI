from colorama import Fore, Style


def __DEFAULT(str: str):
    return str + Style.RESET_ALL


def green(text: str) -> str:
    return __DEFAULT(Fore.GREEN + text)


def blue(text: str) -> str:
    return __DEFAULT(Fore.LIGHTBLUE_EX + text)


def red(text: str) -> str:
    return __DEFAULT(Fore.LIGHTRED_EX + text)


def yellow(text: str) -> str:
    return __DEFAULT(Fore.YELLOW + text)
