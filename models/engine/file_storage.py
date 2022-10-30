#!/usr/bin/python3
"""This is the engine that powers the backend."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Save file instance to JSON."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the address of all the saved instances."""
        return self.__objects

    def new(self, obj):
        """Add new object to file.

        store the address of a new instance from base_model
        create a new instance caling self.reload().
        """
        create_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[create_key] = obj

    def save(self):
        """Save the data to file.

        To successfully save to file, the values must be
        converted to a dictionary
        __objects already have keys but needs the values to be
        converted into a new dictionary so we do not tamper
        the current data dictionary.
        """
        with open(self.__file_path, "w") as new_file:
            convert_obj_to_dict = {}
            for key, value in self.__objects.items():
                convert_obj_to_dict[key] = value.to_dict()
            json.dump(convert_obj_to_dict, new_file)

    def reload(self):
        """Reload data file.

        read data from file and create a new BaseModel instance.
        pass each data to create new instance.
        The value of each key is a dictionary.
        BaseModel(**obj)
        """
        try:
            with open(self.__file_path) as json_file:
                from_json = json.load(json_file)
                for obj in from_json.values():
                    self.new(eval(obj['__class__'])(**obj))
        except FileNotFoundError:
            return
