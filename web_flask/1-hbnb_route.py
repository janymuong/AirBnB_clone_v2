#!/usr/bin/python3
'''module:
multi-routes index(), and some other endpoint else
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''return `Hello, World` text'''
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display “HBNB”'''
    return f'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
