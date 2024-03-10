#!/usr/bin/python3
"""
This is Python3 code, written for a User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that inherits from BaseModel and defines a User for
    our HBNB console
    """
    def __init__(self, *args, **kwargs):
        """
        Function that initializes a User instance
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
