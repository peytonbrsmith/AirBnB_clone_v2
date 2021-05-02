#!/usr/bin/python3
"""
Routes Hello
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world(strict_slashes=False):
    """
    Hello World

    Returns:
        [String] -- [Hello HBNB!]
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
