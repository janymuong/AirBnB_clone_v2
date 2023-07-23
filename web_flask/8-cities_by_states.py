#!/usr/bin/python3
'''module: 8-cities_by_states
includes the Flask web application, SQLAlchemy setup, routes, and templates
'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    '''remove the current SQLAlchemy Session objecf after each request.'''
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    '''Cities, States Endpoint:
    route and the corresponding function to handle the request
    '''
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
