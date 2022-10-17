#!/usr/bin/python3
"""Test for File Storage module """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""
    def test_filestorage(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertFalse(len(storage.all()) == 0)

if __name__ == "__main__":
    unittest.main()