#!/usr/bin/python3
""" BaseModel class for hbnb. """
from datetime import datetime


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    id = ""
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
    
    def __str__(self):
        d = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
