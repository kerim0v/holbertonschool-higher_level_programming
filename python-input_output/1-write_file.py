#!/usr/bin/python3
"""Module writes and returns"""


def write_file(filename="", text=""):
    """ asda """
    with open(filename, "w") as f:
        return f.write(text)
