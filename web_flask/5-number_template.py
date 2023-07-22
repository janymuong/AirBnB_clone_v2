#!/usr/bin/python3
'''module - multi-routes:
define index(), and plus some other endpoints
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''return `Hello, World` text'''
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display “HBNB”'''
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def url_text(text):
    '''
    pass URL parameters to endpoint control
    the 'text' variable will be of type string
    '''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    '''return `Python is cool` text with default or custom text'''
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def print_int(n):
    '''display "n is a number" only if n is an integer'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    pass URL parameters to endpoint control
    the 'n' variable will be of type int
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
