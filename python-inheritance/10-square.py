#!/usr/bin/python3
"""Module for Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """sadadsd"""

    def __init__(self, size):
        """sdadsad"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """dsdas"""
        return self.__size ** 2
