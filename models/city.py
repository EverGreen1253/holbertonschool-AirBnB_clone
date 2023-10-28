#!/usr/bin/python3
""" Nameless module for City class """
from models.base_model import BaseModel


class City(BaseModel):
    """A City class.

    Args:
        None

    Parameters:
        state_id (str): state_id
        name (str): name

    Returns:
        Nothing
    """

    state_id = ""
    name = ""
