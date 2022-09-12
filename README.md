<p align="center">
    <img src=".github/inimod-logo.png" alt="inimod logo">
</p>

<p align="center">
    :snake: A pure Python ini config file reader and generator!
</p>

<p align="center">
<a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://github.com/hrszpuk"><img src="https://img.shields.io/github/followers/hrszpuk?style=social"></a>
<a href="https://twitter.com/hrszpuk"><img src="https://img.shields.io/twitter/follow/hrszpuk?style=social"></a>
<a href="https://github.com/hrszpuk/inimod/issues"><img src="https://img.shields.io/github/issues/hrszpuk/inimod"></a>
</p>

<p align="center">
    inimod is a well documented purely Python config file reader and generator!<br>
    inimod can read .ini files into Python dictionaries, and generate .ini files from Python dictionaries.
</p>

## Usage

### Converting a .ini file to a dictionary
The library will read from a string entered using the `load` function as shown below.

```py
import inimod 

# Read the .ini file and use inimod.load to convert string into a dictionary
with open("example.ini", 'r') as f:
    dictionary = inimod.load(f.read())
```


## Contributors
Contributing helps keep this library safe and up to date. 
If you want to help, why not create an issue?

<a href="https://github.com/hrszpuk/inimod/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hrszpuk/inimod" />
</a>
