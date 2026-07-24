#!/usr/bin/python3
"""
Module task_02_csv

Provides functionality to read data from a CSV file and convert it
into a JSON file (data.json) using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and writes it as JSON to data.json.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
