#!/usr/bin/python3
""" Nameless module for BaseModel class """
import json
import uuid
from datetime import datetime


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

    def __init__(self):
        """Initialize class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """Prints formatted string"""
        return "[BaseModel] ({0}) {1}".format(self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime

        Args:
            None

        Returns:
            Nothing
        """
        self.updated_at = datetime.now()
        # dict_str = str(json.dumps(self.to_dict()))

        # file_name = "BaseModel.json"

        # with open(file_name, "w", encoding="utf-8") as f:
        #     f.write(dict_str)


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
