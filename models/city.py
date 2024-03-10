#!/usr/bin/python3
"""
This is a Python3 code that defines a City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that defines an instance for a city
    a user will pick
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization constructor
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
