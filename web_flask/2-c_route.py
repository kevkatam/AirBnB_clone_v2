#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbn():
    """ function called by route / """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function called  by route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ function callde on route /c/<text> """
    text = text.replace('_',  ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
