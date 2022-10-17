#!/usr/bin/python3
"""This module instantiates an instance of the Storage will be used"""

from os import getenv
from models.city import City
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
