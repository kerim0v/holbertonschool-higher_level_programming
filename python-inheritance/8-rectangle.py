#!/usr/bin/python3
"""saf"""


class BaseGeometry:
    """dasda"""

    def area(self):
        """sada"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """sadad"""

    def __init__(self, width, height):
        """saddsa"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
