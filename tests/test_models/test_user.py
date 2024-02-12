#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    def test_creation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_representation(self):
        user = User()
        str_repr = str(user)
        self.assertIn("[User]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("email", str_repr)
        self.assertIn("password", str_repr)
        self.assertIn("first_name", str_repr)
        self.assertIn("last_name", str_repr)

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

if __name__ == '__main__':
    unittest.main()
