#!/usr/bin/python3
""" Q4 """


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of the specified class
    otherwise False
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class