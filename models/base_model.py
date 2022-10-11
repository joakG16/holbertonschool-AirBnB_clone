#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        It creates a new instance of the class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints data """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        `save` updates the `updated_at` attribute of the object to the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        It converts the object to a dictionary.
        """
        self.updated_at = self.updated_at.isoformat("T")
        self.created_at = self.created_at.isoformat("T")
        newDict = self.__dict__
        newDict["__class__"] = __class__.__name__
        return newDict
