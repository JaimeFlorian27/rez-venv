# rez-venv

a python CLI tool for creating virtual environments based on Rez contexts.

## Installation

### Linux / MacOs
```bash
$ git clone https://github.com/JaimeFlorian27/rez-venv.git
$ cd rez-venv
$ pip install .
```
### Windows (not tested)
```cmd
git clone https://github.com/JaimeFlorian27/rez-venv.git
cd rez-venv
python -m pip install .
```

## Usage
```
usage: rez-venv [-h] [--venv-path [VENV_PATH]] [--system-site-packages [SYSTEM_SITE_PACKAGES]] [--deep-copy [DEEP_COPY]] [packages ...]

Create a virtual environment

positional arguments:
  packages              packages to use in the target environment

optional arguments:
  -h, --help            show this help message and exit
  --venv-path [VENV_PATH]
                        Path to the virtual environment
  --system-site-packages [SYSTEM_SITE_PACKAGES]
                        Give access to the system site-packages
  --deep-copy [DEEP_COPY]
                        create copies of the packages instead of symlinks
```

## TODO

- [ ] Create venv from requirements.txt / context.rtx
- [ ] append rez python package to venv.
- [ ] If good enough distribute on PyPI.