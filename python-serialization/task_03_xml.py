#!/usr/bin/python3
"""
Module task_03_xml

Provides functionality to serialize a Python dictionary to an XML
file, and to deserialize an XML file back into a Python dictionary.
"""
import xml.etree.ElementTree as ET
import ast


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary and saves it to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Loads an XML file and deserializes it into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        try:
            value = ast.literal_eval(child.text)
        except (ValueError, SyntaxError):
            value = child.text
        dictionary[child.tag] = value

    return dictionary
