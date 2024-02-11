#!/usr/bin/python3
""" Task 7 """
from sys import argv


if __name__ == '__main__':
    save_to_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        my_obj = load_from_file(filename)
    except FileNotFoundError:
        my_obj = []

    for arg in argv[1:]:
        my_obj.append(arg)

    save_to_file(my_obj, filename)
