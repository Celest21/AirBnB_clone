import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime

class TestCity(unittest.TestCase):
    def test_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        city = City()
        str_repr = str(city)
        self.assertIn("[City]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("state_id", str_repr)
        self.assertIn("name", str_repr)

    def test_to_dict_method(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)

if __name__ == '__main__':
    unittest.main()

