#!/usr/bin/python3
''' Task 7 '''
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def citystates_list():
    """Display a HTML page """
    statesv = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=statesv)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
