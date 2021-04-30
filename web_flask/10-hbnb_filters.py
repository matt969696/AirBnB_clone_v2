#!/usr/bin/python3
''' Task 7 '''
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page """
    states = storage.all(State)
    amens = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amens=amens)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
