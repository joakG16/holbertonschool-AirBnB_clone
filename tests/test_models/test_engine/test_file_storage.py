#!/usr/bin/python3
""" testing fileStorage """

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from models import storage


class test_file_storage(unittest.TestCase):
    ''' Tests for FileStorage Class '''

    def test_all_method(self):
        inst_ance = BaseModel()
        stor_age = storage.all()
        self.assertIsNotNone(stor_age)
        self.assertEqual(stor_age, storage.all())
        self.assertIs(stor_age, storage.all())

    def test_new_method(self):
        ''' creating a BaseModel instance, which'll call the "new" method,
        then checking if the instance is saved in the file_engine's obj.
        dictionary correctly
        '''
        in_stance = BaseModel()
        ins_id = in_stance.id
        key = f"{in_stance.__class__.__name__}.{ins_id}"
        self.assertIn(key, storage.all().keys())

    def test_reload_method(self):
        """ test for reload method """
        object1 = BaseModel()
        updated_time = object1.__dict__['updated_at']
        object1.save()
        self.assertNotEqual(object1.__dict__['updated_at'], updated_time)
        new_updated_time = object1.__dict__['updated_at']
        storage.reload()
        self.assertEqual(object1.__dict__['updated_at'], new_updated_time)

    def test_file_path(self):
        """ test for the file path existance """
        storageInstance = FileStorage()
        self.assertEqual(storageInstance.path(), "file.json")


if __name__ == '__main__':
    unittest.main()
