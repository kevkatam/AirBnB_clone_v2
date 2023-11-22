#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import shlex
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id """
        objs = models.storage.all()
        citylist = []
        statidlist = []
        for key in objs:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                citylist.append(objs[key])
        for i in citylist:
            if (i.state_id == self.id):
                stateidlist.append(i)
        return (stateidlist)
