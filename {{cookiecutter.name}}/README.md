# {{cookiecutter.name}}

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

{{cookiecutter.description}}

## Environment

- Python {{cookiecutter.runtime}}

## Getting Started

1. create virtualenv
2. activate virtualenv
3. update pip
4. install deps
5. run the python app

> Use `pip install -r requirements-dev.txt` for development.

## Example

### Windows

    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt
    python app.py

### Linux

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip
    pip install -r requirements.txt
    python app.py
