#!/usr/bin/python3
"""Module writes and returns"""


class Student:
    """asdadsadd"""

    def __init__(self, first_name, last_name, age):
        """init chars"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """asdads"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces"""
        for key, value in json.items():
            setattr(self, key, value)
