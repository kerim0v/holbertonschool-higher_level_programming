#!/usr/bin/python3
"""Module writes and returns"""


class Student:
    """asdadsadd"""

    def __init__(self, first_name, last_name, age):
        """init chars"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """asdads"""
        return self.__dict__
