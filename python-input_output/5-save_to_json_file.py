#!/usr/bin/python3
"""Module writes and returns"""
import json


def save_to_json_file(my_obj, filename):
    """sadsd"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
