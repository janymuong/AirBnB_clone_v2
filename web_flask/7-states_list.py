#!/usr/bin/python3
'''module 7-states_list.py
starts a Flask web application - listening on
enpoint: 0.0.0.0:5000/states_list
'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def db_teardown(exception):
    '''remove the current SQLAlchemy Session objecf after each request.'''
    storage.close()


@app.route('/states_list')
def states_list():
    '''Display a HTML page
    with the list of all State objects present in DBStorage.
    '''
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
