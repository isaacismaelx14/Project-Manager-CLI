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

1. Clone the repository
```bash
git clone https://github.com/isaacismaelx14/Project-Manager-CLI.git
cd ./Project-Manager-CLI
```

2. Install `create_component` module

```bash
python setup.py install
```

# How to use 👩‍💻:

Create a component with `default` configuration

```bash
create_component <compnent name>
```

`-c`, `--config`: Create a configuration file.

Example:
```bash
create_component -c
```

`-d`, `--destination`: Change the default destination.

Example:
```bash
create_component <component name> -d <path>
```

# Configuration File ⚙:
> You can use the comand `create_component -c` to create the configuration file.

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
# Version 1.2 updates:
- Now you can install the CLI in your system

# To do 📃:
- [ ] create support for `angular` and `vue.js` components.

_version 1.2_

> With 💖 by [isaacismaelx14](https://github.com/isaacismaelx14)
