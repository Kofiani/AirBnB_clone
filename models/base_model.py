#!/usr/bin/python3
"""This is the base model for the airbnb clone project."""

import uuid
from datetime import datetime


class BaseModel:
    """The Base Model from which all all objects are instantiated."""

    created_at = datetime.today()
    updated_at = datetime.today()

    def __init__(self, *args, **kwargs):
        """Args: use kwargs.

        Pass dictionary to create a new instance/object.
        If parameter is passed create a new instance/object.
        storage.new(self) passes the address of the new instance to storage.
        """
        from models import storage
        if not kwargs:
            self.id = id = str(uuid.uuid4())
            self.created_at = BaseModel.created_at
            self.updated_at = BaseModel.updated_at
            storage.new(self)
        else:
            for key in kwargs:
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])

    def save(self):
        """Save new instance to file.

        Update time if instance is updated.
        storage.save() saves the instance to storage.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Create a dictionary for JSON.

        Convert the data dictionary to be serialized with JSON.
        Create a new key called __class__.
        The new key will be used to create a new object deserializing with JSON.
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        add_class_key = dict(__class__=self.__class__.__name__)
        add_class_key.update(self.__dict__)
        return add_class_key

    def __str__(self):
        """Create a string representation of the object."""
        return '[' + self.__class__.__name__ + ']' +\
                '(' + self.id + ')' + repr(self.__dict__)
