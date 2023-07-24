#!/usr/bin/python3
'''module:
includes the Flask web application, SQLAlchemy setup, routes, and templates
'''

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session objecf after each request.'''
    storage.close()


@app.route('/hbnb_filters')
def filters():
    '''display a HTML page like 6-index.html'''
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
