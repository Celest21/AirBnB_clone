#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage for testing
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the test file if it exists
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_new(self):
        # Test if the new method adds an object to __objects dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.' + obj.id, self.storage.all())

    def test_all(self):
        # Test if the all method returns the __objects dictionary
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_save_and_reload(self):
        # Test if save and reload methods work together
        obj1 = BaseModel()
        obj2 = BaseModel()

        # Save the objects
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear the objects from __objects dictionary
        self.storage._FileStorage__objects = {}

        # Reload the objects
        self.storage.reload()
        all_objs = self.storage.all()

        # Check if the reloaded objects match the original ones
        self.assertIn('BaseModel.' + obj1.id, all_objs)
        self.assertIn('BaseModel.' + obj2.id, all_objs)

        reloaded_obj1 = all_objs['BaseModel.' + obj1.id]
        reloaded_obj2 = all_objs['BaseModel.' + obj2.id]

        self.assertEqual(obj1.to_dict(), reloaded_obj1.to_dict())
        self.assertEqual(obj2.to_dict(), reloaded_obj2.to_dict())

if __name__ == '__main__':
    unittest.main()
