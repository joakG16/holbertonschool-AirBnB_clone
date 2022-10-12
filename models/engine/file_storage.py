#!/usr/bin/python3

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        It returns the list of all objects of the class.
        :return: The list of objects
        """
        return __class__.__objects

    def new(self, obj):
        """
        It sets a new instance/object and adds it to the __objects dictionary.

        :param obj: The object to be added to the dictionary
        """
        # we set a custom key for storing the object
        # key format: <obj class name>.id
        __class__.__objects[obj.__class__.__name__ +
                            "." + obj.id] = obj

    def save(self):
        """
        It saves the dictionary of objects to a file.
        """
        newDict = {}
        # we store the objects dictionary with a custom format
        # provided by the 'to_dict' method
        for key in self.__objects.keys():  # only key
            # a formatted copy of the dict is crated
            newDict[key] = self.__objects[key].to_dict()

        with open(__class__.__file_path, 'w', encoding='utf-8') as jsonFile:
            json.dump(newDict, jsonFile)

    def reload(self):
        """
        It opens the file, reads the data, and creates a new
        instance of the class with the data
        """
        if path.exists(__class__.__file_path):
            # open the file
            with open(__class__.__file_path, 'r') as jsonFile:
                # converts the file content into a dictionary ('data')
                # type(data) = dict
                # Each key value is a dictionary containing the object
                # information
                data = json.loads(jsonFile.read())
                # key will be <object class name>.id format
                # val will be the 'to_dict' formatted dictionary
                for key, val in data.items():
                    # creates the objects and stores them in the class variable
                    __class__.__objects[key] = eval(val["__class__"])(**val)
