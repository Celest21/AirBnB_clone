#!/usr/bin/python3

"""
tests for the base module
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time  # For sleeping between actions

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        """Test object creation and initial attributes"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_save_method(self):
        """Test the save method updates 'updated_at'"""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        time.sleep(1)  # Sleep for a short duration to simulate a time difference
        my_model.save()
        self.assertNotEqual(my_model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, obj_dict)

    def test_str_method(self):
        """Test the __str__ method"""
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertIsInstance(str_representation, str)

if __name__ == '__main__':
    unittest.main()

