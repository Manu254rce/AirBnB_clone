#!/usr/bin/python3
"""
This is Python3 code
"""


import uuid


class BaseModel:
    """
    This class defines all attributes and methods for other classes
    in our console
    """
    def __init__(self):
        """
        This function holds the base attributes/methids used across the project
        """
        self.id = str(uuid.uuid4())