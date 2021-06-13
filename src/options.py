from colors import blue, red, green
from controllers import clearConsole


def start():
    clearConsole()
    use_folder = create_folder_opt()
    use_index = False
    if (use_folder):
        use_index = create_index_file_opt()

    language = language_opt()
    file_type = file_type_opt(language['value'])
    style_type = style_opt()
    use_test = test_opt()

    return {
        'ft': language['result'],
        'ftc': file_type,
        'style_type': style_type['result'],
        'use_test': use_test,
        'use_folder': use_folder,
        'use_index': use_index
    }


def yerOrNO(msg: str) -> str:
    response = input(
        f'------> {blue("[yes/no]")} {red("(default Yes)")}: ').lower()
    value = True
    if(response == 'no' or response == 'not' or response == 'n'):
        value = False

    if value:
        print(f'[{msg} = yes]')
    else:
        print(f"[{msg} = no]")

    return value


def test_opt():
    print(green('\nWill you do tests? '))
    return yerOrNO('Test')


def style_opt():
    print(green('\nWitch type style file do you want to use?'))
    opts = ['none', 'css', 'scss', 'sass']
    style_type = input(
        f"------> {blue(f'[0: {opts[0]}], [1: {opts[1]}], [2: {opts[2]}], [3: {opts[3]}]')} {red(f'(default {opts[1]})')}: ").lower()

    if(style_type == '0' or style_type == 'none'):
        style_type = 0
    elif(style_type == '2' or style_type == 'scss'):
        style_type = 2
    elif(style_type == '3' or style_type == 'sass'):
        style_type = 3
    else:
        style_type = 1

    print(f'[{opts[style_type]}]')
    return {
        'value': style_type,
        'result': opts[style_type]
    }


def file_type_opt(lang: int):
    file_type = 'tsx'
    if(lang == 0):
        print(green('\nWitch type of components file do you want to use for React?'))
        option_type = ['jsx', 'js']
        file_type = input(
            f'------> {blue(f"[0:{option_type[0]}] [1:{option_type[1]}]")} {red(f"(default {option_type[0]})")}: ')

        if(file_type == '1' or file_type == option_type[1]):
            file_type = option_type[1]
        else:
            file_type = option_type[0]

        print(f'[{file_type}]')
    return file_type


def language_opt():
    print(green('\nWitch language do you want to use?'))
    language = input(
        f'------> {blue("[0: javascript] [1: typescript]")} {red(f"(default javascript)")}: ').lower()
    result = 'js'

    if(language == '1'
       or language == 'typescript'
       or language == 'type'
       or language == 'ts'):

        language = 1
        print('[TypeScript]')
        result = 'ts'
    else:
        language = 0
        print('[JavaScript]')

    return {
        'value': language,
        'result': result
    }


def create_index_file_opt():
    print(green('\nDo you want to create an apart index file for this component?'))
    return yerOrNO('Create Index')


def create_folder_opt():
    print(green('\nDo you want to create a folder for this component?'))
    return yerOrNO('Create Folder')
