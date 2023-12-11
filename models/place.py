#!/usr/bin/python3
"""The place module

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Initialize public class attributes"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the place class'''
        super().__init__(*args, **kwargs)
