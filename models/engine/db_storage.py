#!/usr/bin/python3
"""
module for New engine DBStorage alternative storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """ class for DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ initializes the dataa """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ method that queries current database session all objects depending
        of the class name """
        d = {}
        if cls is not None:
            if (type(cls) is str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for i in query:
                key = "{}.{}".format(type(cls).__name__, i.id)
                d[key] = i
        else:
            classlist = [User, State, City, Amenity, Place, Review]
            for c in classlist:
                query = self.__session.query(c)
                for i in query:
                    key = "{}.{}".format(type(c).__name__, i.id)
                    d[key] = i
        return (d)

    def new(self, obj):
        """ adds object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database, create the current database
        session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
