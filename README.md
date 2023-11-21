## JSON-YAML files difference generator
___

### Tests, maintainability and linter status:
[![Actions Status](https://github.com/Unbeliev4ble/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Unbeliev4ble/python-project-50/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/52a3e1b30903d66b16eb/test_coverage)](https://codeclimate.com/github/Unbeliev4ble/python-project-50/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/52a3e1b30903d66b16eb/maintainability)](https://codeclimate.com/github/Unbeliev4ble/python-project-50/maintainability)

### About:
It's a little CLI utility that can help you get demonstration of difference between two files (JSON and/or YAML) in one of proposed formats (stylish, plain or json).


### Installation:
Before installing the package make sure you have [Python 3.10](https://www.python.org/downloads/) (or higher) and [Poetry](https://python-poetry.org/docs/) installed.

*1. Download the package:*

   `git clone git@github.com:Unbeliev4ble/python-project-50.git`


*2. Go to the project main directory:*

   `cd gendiff`

*3. Activate Poetry project manager:*
    
`poetry install`

`poetry build`

*4. Install the package:*

`python3 -m pip install --user dist/*.whl`

### Usage:

`gendiff [-f --format] file_path1 file_path2`

you can get help by typing
`gendiff -h`






### Asciinema demonstarations:
1. Comparing plain.json files. Stylish output format.
[![asciicast](https://asciinema.org/a/d2ltyMMZVjHWAvyvNdsdU3Rnv.svg)](https://asciinema.org/a/d2ltyMMZVjHWAvyvNdsdU3Rnv)
2. Comparing nested.json and .yaml files. Stylish output format.
[![asciicast](https://asciinema.org/a/MgjmJibyu464GkGnSdxCmQuT4.svg)](https://asciinema.org/a/MgjmJibyu464GkGnSdxCmQuT4)
3. Comparing nested.json files. 
Plain output format.
[![asciicast](https://asciinema.org/a/dkMsdK3bsLTXyIhXVRBeqptUx.svg)](https://asciinema.org/a/dkMsdK3bsLTXyIhXVRBeqptUx)