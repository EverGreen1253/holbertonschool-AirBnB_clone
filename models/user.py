#!/usr/bin/python3
""" Nameless module for User class """
from models.base_model import BaseModel


class User(BaseModel):
    """A User class.

    Args:
        None

    Parameters:
        email (str): email
        password (str): password
        first_name (str): the first name
        last_name (str): the last name

    Returns:
        Nothing
    """

    email = None
    password = None
    first_name = None
    last_name = None

    # def __init__(self, *args, **kwargs):
    #     """Initialize class User"""
    #     super().__init__(*args, **kwargs)

    #     if len(kwargs) > 0:
    #         for key in kwargs:
    #             setattr(self, key, kwargs[key])
