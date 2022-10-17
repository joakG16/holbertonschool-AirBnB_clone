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

if __name__ == '__main__':
    unittest.main()