#!/usr/bin/python3
"""
This is a Python script that runs unittests for the console
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TeseHBNBCommand(unittest.TestCase):
    """
    This class defines a series of unittests for our
    HBNB console
    """
    def setUp(self):
        self.mock_stdout = StringIO()
        self.mock_stdin = StringIO()

    def test_do_create(self):
        """
        Function that tests the create command from the CLI
        """
        pass

    def tearDown(self):
        self.mock_stdout.close()
        self.mock_stdin.close()


if __name__ == '__main__':
    unittest.main()
