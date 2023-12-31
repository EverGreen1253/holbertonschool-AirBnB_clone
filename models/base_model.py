#!/usr/bin/python3
""" Nameless module for BaseModel class """
import json
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A BaseModel class.

    Args:
        None

    Parameters:
        id (str): contains the uuid for the model
        created_at (datetime): created datetime
        updated_at (datetime): last updated datetime

    Returns:
        Nothing
    """

    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs):
        """Initialize class BaseModel"""
        if len(kwargs) > 0:
            for key in kwargs:
                if key == 'created_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """Prints formatted string"""
        return "[{0}] ({1}) {2}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime

        Args:
            None

        Returns:
            Nothing
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary of all key value pairs of this instance

        Args:
            None

        Returns:
            Nothing
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__

        return new_dict

    def remove(self):
        """Removes current instance reference from within objects and saves it
        """
        key = self.__class__.__name__ + "." + self.id
        obj = storage.objects
        obj.pop(key)
        storage.objects = obj
        storage.save()
