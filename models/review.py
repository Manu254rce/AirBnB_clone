#!/usr/bin/python3
"""
This is Python3 code that defines a class for Review
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines the reviews that the user will
    make in our HBNB console
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization constructor
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
