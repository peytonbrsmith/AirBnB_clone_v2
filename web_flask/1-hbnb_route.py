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


app.run(host='0.0.0.0')
