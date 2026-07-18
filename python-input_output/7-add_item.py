#!/usr/bin/python3
"""Module writes and returns"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Adds arguments to a list stored in add_item.json"""
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)


main()
