#!/usr/bin/python3
"""
Routes Hello
"""
from flask import Flask
from flask import render_template
from models import storage
from models import State


app = Flask(__name__)


@app.route('/states_list')
def stateslist(strict_slashes=False):
    """
    HBNB

    Returns:
        [Template] -- [HBNB]
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
        Closes Storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
