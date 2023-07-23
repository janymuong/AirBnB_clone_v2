#!/usr/bin/python3
""" Amenity Module for HBNB project """

from os import getenv
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    '''class for amenity:
    like services eg WIFI
    '''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   nullable=False)
        )
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
