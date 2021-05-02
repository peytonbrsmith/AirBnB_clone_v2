#!/usr/bin/python3
"""
Routes Hello
"""
from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def hello_world(strict_slashes=False):
    """
    Hello World

    Returns:
        [String] -- [Hello HBNB!]
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return 'HBNB'


@app.route('/c/<path:subpath>')
def cisfun(subpath, strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return 'C {}'.format(subpath.replace('_', ' '))


@app.route('/python/<path:subpath>')
def pythonwpath(subpath, strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return 'Python {}'.format(subpath.replace('_', ' '))


@app.route('/python/')
def pythonwoutpath(strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return 'Python is cool'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
