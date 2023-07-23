#!/usr/bin/python3
'''
DBStorage module for HBNB project
'''

from os import environ
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'State': State, 'City': City, 'User': User,
           'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage():
    '''DBStorage
    class for managing database storage
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''initialize DBStorage'''
        db_user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{db_user}:{password}@{host}/{db}',
            pool_pre_ping=True
            )

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        '''query all objects from the database'''
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        '''add a new object to the database session'''
        self.__session.add(obj)

    def save(self):
        '''commit changes in the database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete an object from the database session'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''reload database tables and create a new session'''
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        '''close:
        Calls remove() method on the private session attribute (self.__session)
        '''
        self.__session.close()
