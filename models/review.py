#!/usr/bin/python3
"""The review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initialize public class attributes"""
    text = ""
    user_id = ""
    place_id = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)
