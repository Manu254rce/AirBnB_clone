#!/usr/bin/python3
"""
This is a Python3 code that handles file storage
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    This is a class that handles persistent file storage for our console,
    by serializing and deserializing to and from JSON files and vice versa

    Example:
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> ->
        JSON dump -> <class 'str'> -> FILE -> <class 'str'> ->
        JSON load -> <class 'dict'> -> <class 'BaseModel'>
    """

    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self, class_instance):
        """
        Function that returns all dictionary objects
        """
        if class_instance is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items()
                if isinstance(v, class_instance)}

    def new(self, obj):
        """
        Function that adds a new object into storage
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Function that serializes objects into a json file
        """
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict()
                       for k, v in self.__objects.items()}, file)

    def reload(self):
        """
        Function that deserializes the JSON file back
        to objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                objs = json.load(file)
            for obj in objs.values():
                cls_name = obj.pop('__class__', None)
                if cls_name:
                    cls = globals()[cls_name]
                    self.__objects[obj['id']] = cls(**obj)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
