# {{cookiecutter.name}}

## Coding Style

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

## Environment

- Python {{cookiecutter.runtime}}

## Install

    python -m venv venv
    # activate virtualenv
    # Windows: .\venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Usage

    python app.py
