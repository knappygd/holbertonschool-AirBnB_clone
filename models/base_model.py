#!/usr/bin/python3
""" BaseModel class for hbnb. """
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Args:
            args: Unused
            kwargs: Arguments for the BaseModel constructor.

        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
