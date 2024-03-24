#!/usr/bin/python3
"""user.py"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User class

    Attributes:
        email (str): email of user
        password (str): password of user
        first_name (str): first name of user
        last_name (str): last name of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
