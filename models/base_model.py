#!/usr/bin/python3
"""
Module for the BaseModel class.

Blueprint for subclasses

Attributes:
        id: string - assign with an uuid when an object is created
        created_at: datetime - assign with the current datetime when an
                    object is created
        updated_at: datetime - assign with the current datetime when an
                    object is created and it will be updated every time
                    you change your object
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """time format for datetime conversion"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        """a unique ID for the instance"""
        self.id = str(uuid.uuid4())
        """creation and update timestamps to the current UTC time"""
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        """If keyword arguments are provided, update instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Save the current state of the instance and update the storage
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Convert the instance to a dictionary representation
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
