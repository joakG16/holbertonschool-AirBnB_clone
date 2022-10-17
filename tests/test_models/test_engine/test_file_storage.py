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

    def test_save_method(self):
        pass

    def test_reload_method(self):
        """ test for reload method """
        storage = FileStorage()
        storage.reload()
        self.assertIsNotNone(storage.all())


if __name__ == '__main__':
    unittest.main()
