#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Initialize public class attributes"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the Amenity class"""
        super().__init__(*args, **kwargs)
