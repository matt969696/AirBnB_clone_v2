#!/usr/bin/python3
''' Task 7 '''
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page """
    states = storage.all(State)
    id = None
    return render_template("9-states.html", states=states, id=id)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page """
    states = storage.all(State)
    id = 'State.' + str(id)
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
