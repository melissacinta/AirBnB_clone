#!/usr/bin/python3
"""
Defines the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Initialize public class attribute"""
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the state class'''
        super().__init__(*args, **kwargs)
