# HNGR-ISP-Categorization
# HNGR-ISP-Categorization

## Setup Development Environment

### Windows

*Prefered method is to setup WSL. But you can also proceed without*

1. Install WSL and Debian

Refer to [Microsoft's install guide](https://learn.microsoft.com/en-us/windows/wsl/install)

Then install Debian from the Microsoft store: [link](https://www.microsoft.com/en-us/p/debian/9msvkqc78pk6)

3. update system to latest version

`sudo apt update && sudo apt upgrade`

2. Install packages needed for Development

`sudo apt install git python3 python3.11-venv`

3. Create a new python venv for installing packages

`python3 -m venv ~/.virtualenvs/djangodev`

4. Activate the python venv environment.

`source ~/.virtualenvs/djangodev/bin/activate`

NOTE: you must do this every time you work on this project, and have "deactivated" or closed the terminal window.

4. Install django

`python -m pip install Django`

5. Clone the HNGR repo

`git clone https://github.com/ekirchman/HNGR-ISP-Categorization-Backend.git`

6. Start the server

`python manage.py runserver`


### MacOS

1. Install [homebrew](https://brew.sh/) package manager by running the following line in your terminal:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Install python 3.12 and other dev tools

`brew install git python@3.12`

3. Create a new python venv for installing packages

`python3 -m venv ~/.virtualenvs/djangodev`

4. Activate the python venv environment.

`source ~/.virtualenvs/djangodev/bin/activate`

NOTE: you must do this every time you work on this project, and have "deactivated" or closed the terminal window.


5. Install django

`python -m pip install Django`

6. Clone the HNGR repo

`git clone https://github.com/ekirchman/HNGR-ISP-Categorization-Backend.git`

7. Start the server

`python manage.py runserver`

### Linux

1. Install python 3.12 and other dev tools through your package manager

2. Create a new python venv for installing packages

`python3 -m venv ~/.virtualenvs/djangodev`

3. Activate the python venv environment.

`source ~/.virtualenvs/djangodev/bin/activate`

NOTE: you must do this every time you work on this project, and have "deactivated" or closed the terminal window.


4. Install django

`python -m pip install Django`

6. Clone the HNGR repo

`git clone https://github.com/ekirchman/HNGR-ISP-Categorization-Backend.git`

7. Start the server

`python manage.py runserver`
