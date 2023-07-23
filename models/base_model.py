#!/usr/bin/python3
'''module for Base class:
for subclassing
this module defines a base class for all models in our hbnb clone'''

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = '%Y-%m-%dT%H:%M:%S.%f'

if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    '''A base class for all hbnb models'''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        '''constructor
        instantiates a new model
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        '''returns a string representation of the instance'''
        return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        '''
        updates updated_at with current timestamp when instance is changed
        '''
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''converts instance into dict format - returns key/value pairs'''
        obj_dict = self.__dict__.copy()
        if 'created_at' in obj_dict:
            obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
        obj_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in obj_dict:
            del obj_dict['_sa_instance_state']
        return obj_dict

    def delete(self):
        '''deletes the current instance from storage'''
        models.storage.delete(self)
