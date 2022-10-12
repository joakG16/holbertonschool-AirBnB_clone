#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary of stored objects
        """
        return __class__.__objects

    def new(self, obj):
        """
        It sets a new instance/object and adds it to the __objects dictionary.

        :param obj: The object to be added to the dictionary
        """
        __class__.__objects[obj.__class__.__name__ +
                            "." + obj.id] = obj

    def save(self):
        """
        It opens the file in write mode, dumps the contents
        of __objects into the file, and closes the file.
        It is basically serializng the dictionary of obj.
        into the json file.
        """
        newDict = {}
        for key in self.__objects.keys():  # only key
            ''' setting values through indexing '''
            newDict[key] = self.__objects[key].to_dict()

        with open(__class__.__file_path, 'w', encoding='utf-8') as jsonFile:
            json.dump(newDict, jsonFile)

    def reload(self):
        """
        It reads the file and loads the data into the __objects variable
        """
        if path.exists(__class__.__file_path):
            with open(__class__.__file_path, 'r') as jsonFile:
                data = json.loads(jsonFile.read())
                for key, value in data.items():
                    __class__.__objects[key] = eval(
                        value["__class__"])(**value)
