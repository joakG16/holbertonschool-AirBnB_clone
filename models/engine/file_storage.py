#!/usr/bin/python3

import json
from os import path


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary of objects
        """
        return __class__.__objects

    def new(self, obj):
        """
        It sets a new object and adds it to the __objects dictionary.

        :param obj: The object to be added to the dictionary
        """
        __class__.__objects[obj.__class__.__name__ +
                            "." + obj.id] = obj.__dict__

    def save(self):
        """
        It opens the file in write mode, dumps the contents
        of __objects into the file, and closes the file
        """
        with open(__class__.__file_path, 'w') as jsonFile:
            jsonFile.write(json.dumps(__class__.__objects, default=str))

    def reload(self):
        """
        It reads the file and loads the data into the __objects variable
        """
        if path.exists(__class__.__file_path):
            with open(__class__.__file_path, 'r') as jsonFile:
                __class__.__objects = json.loads(jsonFile.read())
