#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="delete", backref="state")

    @property
    def cities(self):
        """ cities getter attribute """
        cit_lis = []
        for k, v in models.storage.all().items():
            if v.state_id == self.id:
                cit_lis.append(v)
            return cit_lis
