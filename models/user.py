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

    email = ""
    password = ""
    first_name = ""
    last_name = ""
