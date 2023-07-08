#!/usr/bin/python3
""" Unittest for Test File storage. """
import json
import os
import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_adds_instance_to_objects(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)
        self.assertIn(key, self.storage.all())

    def test_save_writes_to_file(self):
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.storage.new(obj)

        temp_file = "temp_file.json"
        self.storage._FileStorage__file_pathkkoijk = temp_file

        self.storage.save()

        with open(temp_file, "r") as file:
            data = json.load(file)
            self.assertIn(key, data)
        os.remove(temp_file)


if __name__ == "__main__":
    unittest.main()
