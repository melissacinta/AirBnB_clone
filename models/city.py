#!/usr/bin/python3
"""The `city` module

"""
from models.base_model import BaseModel


class City(BaseModel):
    """Initialize public class attributes"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for the city class"""
        super().__init__(*args, **kwargs)
