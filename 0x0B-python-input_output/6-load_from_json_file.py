#!/usr/bin/python3
""" Task 6 """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r') as data:
        my_dict = json.load(data)
    return my_dict
