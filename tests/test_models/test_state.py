import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime

class TestState(unittest.TestCase):
    def test_creation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        state = State()
        str_repr = str(state)
        self.assertIn("[State]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("name", str_repr)

    def test_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("name", state_dict)

if __name__ == '__main__':
    unittest.main()

