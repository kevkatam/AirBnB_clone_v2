#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    name = "" 
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id """
        allCities = models.storage.all(City)
        citylist = []
        for city in allCities.values():
            if city.state_id == self.id:
                citylist.append(city)
        return (citylist)
