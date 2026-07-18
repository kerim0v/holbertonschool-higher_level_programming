#!/usr/bin/python3
"""Module that reads and prints the content of a UTF8 text file"""


def read_file(filename=""):
    """Reads and prints"""
    
    with open(filename, r) as f:
        content = f.read()
        print(content)
