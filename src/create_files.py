import os
from colors import blue, green, red
from pathlib import Path
from errorManager import ErrorExp


def check_exist(path):
    path = Path(path)
    if(path.is_file()):
        raise ErrorExp(red(f'File {path.name} already exists'))


def create_test_js(fileAbsoulte, fn, ft, using_index):
    file_name = f'{fileAbsoulte}.test.{ft}'
    check_exist(file_name)
    file = open(file_name, "w")
    file.write('import React from "react";\n')
    file.write('import "@testing-library/jest-dom";\n')
    file.write('import { render } from "@testing-library/react";\n')
    file.write(f'import {fn} from ')
    if(using_index):
        file.write(f'"./"')
    else:
        file.write(f'"./{fn}"')
    file.write(';'+os.linesep)
    file.write(f'describe("<{fn} />", () => '+'{\n')
    file.write('  let component;\n')
    file.write('  beforeEach(() => {\n')
    file.write(f'    component = render(<{fn} />);\n')
    file.write('  });'+os.linesep)
    file.write('  test("should render", () => {\n')
    file.write(f'    component.getByText("{fn}");\n')
    file.write('  });\n')
    file.write('});')
    print(f'{blue(f"{fn}.test.{ft}")} {green("created")}')


def create_style(filePath, fn, styleType):
    styleFile = f'{fn}.{styleType}'
    stylePath = Path(filePath, styleFile)
    check_exist(stylePath)
    file = open(f'{stylePath}', "w")
    file.write(f'.{fn.lower()}_component'+'{\n')
    file.write(f'  color:red;\n')
    file.write('}')
    print(f'{blue(styleFile)} {green("created")}')


def create_jsx(fileAbsoulte, fn, styleType, ftc):
    file_name = f'{fileAbsoulte}.{ftc}'
    check_exist(file_name)
    file = open(file_name, "w")
    if styleType != "none":
        file.write(f'import "./{fn}.{styleType}" \n')
    file.write(f'function {fn}()'+'{ \n')
    file.write('  return (\n')
    file.write(f'    <section className="{fn.lower()}_component">\n')
    file.write(f'      <h2>{fn}</h2>\n')
    file.write('    </section>\n')
    file.write('  );\n')
    file.write('}' + os.linesep)
    file.write(f'export default {fn};')
    print(f'{blue(f"{fn}.{ftc}")} {green("created")}')


def create_index(filePath, fn, ft):
    fileAbsoulteIndex = Path(filePath, f'index.{ft}')
    check_exist(fileAbsoulteIndex)
    file = open(fileAbsoulteIndex, "w")
    file.write('export { default } '+f'from "./{fn}"')
    file.close()
    print(f'{blue(f"index.{ft}")} {green("created")}')
