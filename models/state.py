#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="delete", backref="state")

    @property
    def cities(self):
        """ cities getter attribute """
        cit_lis = []
        for v in models.storage.all(City).values():
            if v.state_id == self.id:
                cit_lis.append(v)
            return cit_lis
