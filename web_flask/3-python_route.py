#!/usr/bin/python3
''' Task 1 '''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Hello HBNB! '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def just_hbnb():
    ''' HBNB '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_what(text):
    ''' c is something '''
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    ''' Python is cool '''
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
