#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models.amenity import Amenity


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
