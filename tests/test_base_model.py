#!/usr/bin/python3
"""
This is Python code for a unittest of our BaseModel class
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This is a class that performs a unit test on a given module
    for our project
    """

    def setUp(self):
        """
        This function creates instances for our BaseModel class
        """
        self.base_model_obj = BaseModel()

    def test_kwargs(self):
        """
        Function that kwargs is correctly set
        """
        test_kwargs = {
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            '__class__': 'BaseModel'
        }

        test_obj = BaseModel(**test_kwargs)
        self.assertEqual(test_obj.id, 'test_id')
        self.assertIsInstance(test_obj.created_at, datetime)
        self.assertIsInstance(test_obj.updated_at, datetime)

    def test_uuid(self):
        """
        This function ensures that uuid from BaseModel is always a string
        """
        self.assertIsNotNone(self.base_model_obj.id)
        self.assertIsInstance(self.base_model_obj.id, str)

    def test_datetime(self):
        """
        Function that tests the datetime attributes
        """
        self.assertIsNotNone(self.base_model_obj.created_at)
        self.assertIsNotNone(self.base_model_obj.updated_at)
        self.assertIsInstance(self.base_model_obj.created_at, datetime)
        self.assertIsInstance(self.base_model_obj.updated_at, datetime)

    def test_save(self):
        """
        Function that ensures that the updated_at
        attribute has been saved succesfully
        """
        old_updated_at = self.base_model_obj.updated_at
        self.base_model_obj.save()
        self.assertNotEqual(old_updated_at, self.base_model_obj.updated_at)

    def test_str_representation(self):
        """
        Function that tests the string representation of the BaseModel instance
        """
        exp_str = (
            f"[BaseModel] ({self.base_model_obj.id}) "
            f"{self.base_model_obj.__dict__}"
        )
        self.assertEqual(str(self.base_model_obj), exp_str)

    def test_serialization(self):
        """
        Function that tests the serialization process to a dictionary object
        """
        base_model_dict = self.base_model_obj.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], self.base_model_obj.id)
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
