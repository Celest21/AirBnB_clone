#!/usr/bin/python3

import json
import os
from datetime import datetime


class FileStorage:
    """Defines the blueprint of saving and retrieving objects .

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def all(self):
        """
        Returns the __objects dictionary.
        It provides access to all the stored objects.
        """
        return self.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}

        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as file:
                    data = json.load(file)

                    for key, obj_data in data.items():
                        class_name, obj_id = key.split('.')
                        module = __import__('models')
                        class_ = getattr(module, class_name)
                        obj = class_(**obj_data)
                        self.__objects[key] = obj

            except json.JSONDecodeError:
                pass  # Handle JSON decoding error if needed
