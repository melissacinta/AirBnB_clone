#!/usr/bin/python3
"""
 defines user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Initialize public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the Amenity class'''
        super().__init__(*args, **kwargs)
