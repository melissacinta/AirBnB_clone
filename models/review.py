#!/usr/bin/python3
"""The review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    text = ""
    user_id = ""
    place_id = ""
