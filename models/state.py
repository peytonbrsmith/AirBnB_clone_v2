#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', cascade="delete", backref='state')

    