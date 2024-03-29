#!/usr/bin/python3
"""
This is a Python3 code, that creates a class for State
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    This class defines an instance for the state
    and inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization constructor
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
