#!/usr/bin/python3
"""
 defines user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Initialize instance attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
