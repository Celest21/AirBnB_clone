#!/usr/bin/python3
"""
Basemodel: this module has a class that defines 
all other classes for this project
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Blueprint for the subclasses

    Attributes:
    id: string - assign with an uuid when an instance is created
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created

    """

    def __init__(self):
        """Object constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method to create a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

