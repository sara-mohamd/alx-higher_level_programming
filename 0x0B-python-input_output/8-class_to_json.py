#!/usr/bin/python3
""" Task 8 """


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """
    return obj.__dict__
