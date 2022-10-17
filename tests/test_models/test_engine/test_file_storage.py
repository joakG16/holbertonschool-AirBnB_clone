#!/usr/bin/python3
"""Test for File Storage module """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage"""

    def test_filestorage(self):
        """
        Test filestorage
        """
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertFalse(len(storage.all()) == 0)

    def test_file_path(self):
        """
        Test method to check file name
        """
        storage = FileStorage()
        self.assertEqual(storage.path(), "file.json")


if __name__ == "__main__":
    unittest.main()
