#!/usr/bin/python3
""" Nameless module for Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """A Place class.

    Args:
        None

    Parameters:
        city_id (str): city_id
        user_id (str): user_id
        name (str): name
        description (str): description
        number_rooms (int): number_rooms
        number_bathrooms (int): number_bathrooms
        max_guest (int): max_guest
        price_by_night (int): price_by_night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): amenity_ids

    Returns:
        Nothing
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
