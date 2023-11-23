#!/usr/bin/python3
"""
module for New engine DBStorage alternative storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
import sqlalchemy


class DBStorage:
    """ class for DBStorage """
    __engine = None
    __session = None

    classes = {"User": User, "State": State, "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def __init__(self):
        """ initializes the dataa """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        dic = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                query = self.__session.query(classes[c]).all()
                for elem in query:
                    key = "{}.{}".format(elem.__class__.__name__, elem.id)
                    dic[key] = elem
        return (dic)

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
