#!/usr/bin/python3
"""
This is Python code for a unittest
"""


import unittest
from console import hello


class TestConsole(unittest.TestCase):
    """
    This is a class that performs a unit test on a given module
    for our project
    """
    def test_console(self):
        """
        Function responsible for the unittest
        """
        self.assertEqual(hello(), "Hello World")


if __name__ == "__main__":
    unittest.main()
