# Project Manager CLI ⭐ [!["Pyhton"](https://img.shields.io/badge/python-3.9.1%20-gray.svg?longCache=true&logo=python&colorB=yellow)](https://www.python.org/downloads/release/python-391/)

With this script you have a template for create react components with some default files as:
 
**Template example:**

```
Component
├── index.js
├── Component.jsx
├── Component.css
├── Component.test.js
```
> You can create your own template and have support for `Typescript's components` and to use `scss` or `sass`; you can also select if you want to use an `index file`, `style file`, `test file` and if you want your component `inside a folder` or `no`

# Index 👇

- [First steps 🦶:](#first-steps-)
- [Commands 👩‍💻:](#commands-)
- [Configuration File ⚙:](#configuration-file-)
  * [Example:](#example)
  * [Attributes:](#attributes)
    + [component:](#component)
- [Version 1.1 updates:](#version-11-updates)
- [To do 📃:](#to-do-)

# First steps 🦶:

1. `$ git clone https://github.com/isaacismaelx14/Project-Manager-CLI.git`
2. `$ cd ./Project-Manager-CLI`
3. `$ pip install -r requirements.txt` or with **pipenv**: `$ pipenv install --ignore-pipfile`
4. `$ python ./src/app.py `

# Commands 👩‍💻:
`$ python ./src/app.py  [Component Name]`: create a component directly

`-c`, `--config`: Create a configuration file.

`-d`, `--destination`: Change the default destination.

# Configuration File ⚙:
> You can use the comand `$ python ./src/app.py -c` to create the configuration file.

## Example: 
`PManager.json`
```json
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

## Attributes:
> `lang attribute` is not supported yet.

| Key| Type| Value| Description|
| ----- | ---- | ---- | ---- |
| dir | String |\*|Path of the folder where you want to create your `components`|
| lang | String |`react` \| `angular` \| `vue.js`|`NOT SUPPORTED`. This will be used for define the type of `component` that your project use. Exp: `react`, `angular` or `vue.js`. Now only support for `react`|
| component | Object | `lang` \| `component_file_type` \| `use_test` \| `use_folder` \| `use_index` |contain the `component configuration`|


### component:
| Key| Type| Value| Description|
| ----- | ---- | ---- | ---- |
| lang | String | `js` \| `ts` |define the language of your project `js` for `Javascript` and `ts` for `Typescript`|
|component_file_type | String | `jsx` \| `js` \| `tsx` |define if you want to use `js` file for your components or `jsx` file. (if your `componet -> lang` is `ts` default is `tsx`)|
| use_test | Boolean |`true` \| `false`|define if you want to create and `test file` for `unit test`|
| use_folder | Boolean |`true` \| `false`|define if you want that your `component's files` are inside and folder|
| use_index | Boolean |`true` \| `false`|define if you want that your `component's folder` have an `index` file to link to your `component` (useful is you are using a lot of components)|
# Version 1.1 updates:
- Config file for projects
- More simple commnad
- New CLI
- use the destination of the config file or set on the command with `-d` or `--destinantion`

# To do 📃:
- [ ] create support for `angular` and `vue.js` components.

_version 1.1_

> With 💖 by [isaacismaelx14](https://github.com/isaacismaelx14)
