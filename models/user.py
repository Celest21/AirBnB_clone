#!/usr/bin/python3

"""
Module for the User class.
"""

from models.base_model import BaseModel


class User(User):
    """
    User class that inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
