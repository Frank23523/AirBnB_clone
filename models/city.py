#!/usr/bin/python3
"""city.py"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City class.

    Attributes:
        state_id (str): state id
        name (str): name of the city
    """

    state_id = ""
    name = ""
