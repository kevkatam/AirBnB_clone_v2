#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ function called on route /python/<text> """
    if text is not "is cool":
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ function called on route /number/<n> """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ function called on route /number_template/<n> """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ function called on route /number_odd_or_even/<n> """
    if n % 2 == 0:
        text = f"{n} is even"
    else:
        text = f"{n} is odd"
    return render_template('6-number_odd_or_even.html', value=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
