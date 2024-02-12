import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime

class TestReview(unittest.TestCase):
    def test_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        review = Review()
        str_repr = str(review)
        self.assertIn("[Review]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)
        self.assertIn("place_id", str_repr)
        self.assertIn("user_id", str_repr)
        self.assertIn("text", str_repr)

    def test_to_dict_method(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

if __name__ == '__main__':
    unittest.main()

