#!/usr/bin/python3
"""Module writes and returns"""


def append_write(filename="", text=""):
    """asas"""
    with open(filename, "a") as f:
        return f.write(text)
