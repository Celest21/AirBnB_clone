import unittest
import os
import json
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.obj1 = User()
        self.obj2 = State()
        self.obj3 = City()
        self.obj4 = Amenity()
        self.obj5 = Place()
        self.obj6 = Review()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_method(self):
        self.file_storage.new(self.obj1)
        self.assertEqual(len(self.file_storage.all()), 1)
        self.assertIn("User." + self.obj1.id, self.file_storage.all())

    def test_all_method(self):
        self.assertEqual(self.file_storage.all(), {})

        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)

        all_objects = self.file_storage.all()

        self.assertEqual(len(all_objects), 2)
        self.assertIn("User." + self.obj1.id, all_objects)
        self.assertIn("State." + self.obj2.id, all_objects)

    def test_save_method(self):
        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)

        self.file_storage.save()

        with open(self.file_path, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        self.assertIn("User." + self.obj1.id, saved_data)
        self.assertIn("State." + self.obj2.id, saved_data)

    def test_reload_method(self):
        self.file_storage.new(self.obj1)
        self.file_storage.new(self.obj2)

        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        reloaded_objects = new_file_storage.all()

        self.assertEqual(len(reloaded_objects), 2)
        self.assertIn("User." + self.obj1.id, reloaded_objects)
        self.assertIn("State." + self.obj2.id, reloaded_objects)

    def test_reload_method_file_not_exist(self):
        # Test when the file does not exist
        self.file_storage.reload()

        reloaded_objects = self.file_storage.all()

        self.assertEqual(reloaded_objects, {})

if __name__ == '__main__':
    unittest.main()

