#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, City
from sqlalchemy import Column, Integer, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column('city_id', String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column('user_id', String(60), nullable=False, ForeignKey('users.id'))
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=False)
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column('number_bathrooms', Integer, nullable=False, default=0)
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column('price_by_night', Integer, nullable=False, default=0)
    latitude = Column('latitude', Float, nullable=True)
    longitude = Column('longitude', Float, nullable=True)
    # amenity_ids = []
