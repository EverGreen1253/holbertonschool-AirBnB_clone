#!/usr/bin/python3
""" Nameless module for Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class.

    Args:
        None

    Parameters:
        place_id (str): place_id
        user_id (str): user_id
        text (str): text

    Returns:
        Nothing
    """

    place_id = ""
    user_id = ""
    text = ""
