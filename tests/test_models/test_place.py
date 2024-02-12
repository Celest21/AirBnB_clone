import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime

class TestPlace(unittest.TestCase):
    def test_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(place.amenity_ids, [])

    def test_str_representation(self):
        place = Place()
        str_repr = str(place)
        self.assertIn("[Place]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("city_id", str_repr)
        self.assertIn("user_id", str_repr)
        self.assertIn("name", str_repr)
        self.assertIn("description", str_repr)
        self.assertIn("number_rooms", str_repr)
        self.assertIn("number_bathrooms", str_repr)
        self.assertIn("max_guest", str_repr)
        self.assertIn("price_by_night", str_repr)
        self.assertIn("latitude", str_repr)
        self.assertIn("longitude", str_repr)
        self.assertIn("amenity_ids", str_repr)

    def test_to_dict_method(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("__class__", place_dict)
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenity_ids", place_dict)

if __name__ == '__main__':
    unittest.main()

