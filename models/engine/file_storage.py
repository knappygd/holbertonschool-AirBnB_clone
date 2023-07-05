#!/usr/bin/python3
""" Serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(self).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        sdict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w") as file:
            json.dump(sdict, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                for k, v in (json.load(file)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except FileNotFoundError:
            pass
