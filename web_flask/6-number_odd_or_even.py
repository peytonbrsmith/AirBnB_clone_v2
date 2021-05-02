#!/usr/bin/python3
"""
Routes Hello
"""
from flask import Flask
from flask import render_template
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


@app.route('/number/<int:number>')
def number(number, strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return "{} is a number".format(number)


@app.route('/number_template/<int:number>')
def numbertemplate(number, strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>')
def numbereo(number, strict_slashes=False):
    """
    HBNB

    Returns:
        [String] -- [HBNB]
    """
    return render_template('6-number_odd_or_even.html', number=number)

app.run(host='0.0.0.0')
