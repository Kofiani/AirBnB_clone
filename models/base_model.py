#!/usr/bin/python3
''' This is the base model for the airbnb clone project'''

import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = datetime.today()

    def __init__(self):
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at
        self.updated_at = BaseModel.updated_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        add_class_key = dict(__class__ = self.__class__.__name__)
        add_class_key.update(self.__dict__)
        return add_class_key

    def __str__(self):
        return '[' + self.__class__.__name__ + ']' + '(' + self.id + ')' + repr(self.__dict__)
