#!/usr/bin/python3
""" Unittest for Test File storage. """
import json
import os
import unittest
import models
from unittest.mock import patch, mock_open
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
    def tearDown(self):
        """
            delete the file.json when finish the test
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

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
    def test_models_storage(self):
        """
            test if storage in init is on
        """
        self.assertIsNotNone(models.storage.all())
        self.assertIsNone(models.storage.reload())

    def test_save_reload(self):
        """
            test save and reload method
        """
        self.storage.new(self.model1)
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        obj_key = "BaseModel." + self.model1.id
        obj_all = self.storage.all()
        obj_storage = obj_all[obj_key]
        self.assertIn(obj_key, self.storage.all())
        self.assertTrue(self.model1.__dict__ == obj_storage.__dict__)
        self.assertFalse(self.model1 is obj_storage)
        self.assertIsInstance(obj_storage, BaseModel)
        self.assertEqual(self.model1.id, obj_storage.id)


if __name__ == "__main__":
    unittest.main()
