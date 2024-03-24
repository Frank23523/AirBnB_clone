#!/usr/bin/python3
"""review.py"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review class.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
