#!/usr/bin/python3
""" BaseModel class for hbnb. """
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.

    Attributes:
        id: BaseModel id.
        created_at: Date and time at creation.
        updated_at: Date and time of last update.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ Updates `updated_at` with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing
        all keys/values of __dict__ of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """ Returns a string containing the class name, id and dictionary. """
        d = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
