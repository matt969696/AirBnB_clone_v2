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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
