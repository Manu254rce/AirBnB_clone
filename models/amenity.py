#!/usr/bin/python3
"""
This is a Python3 code that defines a class for an amenity
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class defines an amenity instance for our
    HBNB console
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization constructor
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
