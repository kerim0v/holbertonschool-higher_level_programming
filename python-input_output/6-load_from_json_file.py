#!/usr/bin/python3
"""Module writes and returns"""
import json


def load_from_json_file(filename):
    """sdasd"""
    with open(filename, "r") as f:
        return json.load(f)
