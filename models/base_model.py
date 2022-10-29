#!/usr/bin/python3
'''This is the base model for the airbnb clone project'''

import uuid
from datetime import datetime


class BaseModel:
    '''The Base Model from which all all objects
        are instantiated'''
    created_at = datetime.today()
    updated_at = datetime.today()

    def __init__(self, *args, **kwargs):
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
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        add_class_key = dict(__class__=self.__class__.__name__)
        add_class_key.update(self.__dict__)
        return add_class_key

    def __str__(self):
        return '[' + self.__class__.__name__ + ']' +\
                '(' + self.id + ')' + repr(self.__dict__)
