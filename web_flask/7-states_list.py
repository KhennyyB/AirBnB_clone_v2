#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
        Automatically remove session at end of request or
        app shutdown
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """
        display html jinja format of state name and id
    """
    all_objs = storage.all(State).values()
    return render_template('7-states_list.html', all_objs=all_objs)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
