#!/usr/bin/python3
""" Nameless module for FileStorage class """
import json
import sys
import os


class FileStorage:
    """A FileStorage class.

    Args:
        None

    Parameters:
        __file_path (str): path to the JSON file
        __objects (dict): stores all objects by <class name>.id

    Returns:
        Nothing
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Initialize class FileStorage"""

    @property
    def file_path(self):
        """Getter for private prop file_path

            Returns:
                value of __file_path
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        """Sets value of file_path.

            Returns:
                Nothing
        """

        self.__file_path = value

    @property
    def objects(self):
        """Getter for private prop objects

            Returns:
                value of __objects
        """
        return self.__objects

    @objects.setter
    def objects(self, value):
        """Sets value of objects.

            Returns:
                Nothing
        """

        self.__objects = value

    def all(self):
        """Returns all data in dictionary form"""
        return self.objects

    def new(self, obj):
        """Sets the obj data into __objects"""
        key = obj.__class__.__name__ + "." + obj.id
        self.objects[key] = obj

    def save(self):
        """Serialises __objects data into JSON format in the file specified by __file_path"""
        serialised = {}
        for key in self.objects:
            serialised[key] = self.objects[key].to_dict()

        data = str(json.dumps(serialised))

        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(str(data))

    def reload(self):
        """Reads the JSON data from file specified at __file_path"""
        from models.base_model import BaseModel

        data = ""
        if os.path.isfile(self.file_path) is True:
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        data += line
            except IOError:
                pass

            serialised = json.loads(data)

            for key in serialised:
                s = serialised[key]
                kwargs = {}
                for k in s:
                    kwargs[k] = s[k]

                b = BaseModel(**kwargs)

                self.objects[key] = b
