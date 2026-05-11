#!/usr/bin/python3
"""
This module provides a function that prints a square using the # character.
"""


def print_square(size):
    """
    Prints a square of # characters with the given size.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is a negative float.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
