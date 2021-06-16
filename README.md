# Project Manager CLI ⭐ [!["Pyhton"](https://img.shields.io/badge/python-3.9.1%20-gray.svg?longCache=true&logo=python&colorB=yellow)](https://www.python.org/downloads/release/python-391/)

with this script you have a template for create react components with some default files as:


- Component (Component folder) [optional]
  - index.js (can be: .ts) [optional]
  - Component.jsx (can be: .js or .tsx)
  - Component.css (can be:  .css, .scss or .sass)  [optional]
  - Component.test.js [optional]


## First steps 🦶:

1. `$ git clone https://github.com/isaacismaelx14/Project-Manager-CLI.git`
2. `$ cd ./Project-Manager-CLI`
3. `$ pip install -r requirements.txt` or with **pipenv**: `$ pipenv install --ignore-pipfile`
4. `$ python ./src/app.py `

## Commands 👩‍💻:
`$ python ./src/app.py  [Component Name]`: create a component directly

`-c`, `--config`: Create a configuration file.

`-d`, `--destination`: Change the default destination.

## Configuration File ⚙:
> You can use the comand `$ python ./src/app.py -c` to create the configuration file.

- "dir": `Components path`

- "lang": _This will be useful in later versions._

- "component": `Object`

  - "lang": `js` | `ts`
  - "component_file_type": `jsx` | `js` | `tsx`
  - "style_type": `css` | `scss` | `sass` | `none`
  - "use_test": `true` | `false`
  - "use_folder": `true` | `false`
  - "use_index": `true` | `false`


**Example:**
```
{
  "dir": "src/components",
  "lang": "react",
  "component": {
    "lang": "js",
    "component_file_type": "jsx",
    "style_type": "css",
    "use_test": true,
    "use_folder": true,
    "use_index": true
  }
}
```

## Version 1.1 updates:
- Config file for projects
- More simple commnad
- New CLI
- use the destination of the config file or set on the command with `-d` or `--destinantion`

_version 1.1_

> With 💖 by [isaacismaelx14](https://github.com/isaacismaelx14)
