#!/usr/bin/python3
"""
This is Python code for a unittest
"""


import unittest
from models import base_model


class TestConsole(unittest.TestCase):
    """
    This is a class that performs a unit test on a given module
    for our project
    """
    def test_uuid(self):
        """
        This function ensures that uuid from BaseModel is always a string
        """
        base_model_obj = base_model.BaseModel()
        self.assertIsNotNone(base_model_obj.id)
        self.assertIsInstance(base_model_obj.id, str)
    def test_console(self):
        """
        Function responsible for the unittest
        """
        pass


if __name__ == "__main__":
    unittest.main()
