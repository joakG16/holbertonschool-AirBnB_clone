#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        It creates a new instance of the class.
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'my_number':
                    self.my_number = value
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'name':
                    self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ returns string representation of the object """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        `save` updates the `updated_at` attribute of the object to the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        It converts the object to a dictionary.
        """
        newDict = self.__dict__.copy()
        newDict['updated_at'] = self.updated_at.isoformat("T")
        newDict['created_at'] = self.created_at.isoformat("T")
        newDict["__class__"] = __class__.__name__
        return newDict
