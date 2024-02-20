#!/usr/bin/python3
""" 1st task """
import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Return JSON string representation """
        if list_dictionaries is not None:
            new_json = json.dumps(list_dictionaries)
            return new_json
        else:
            return "[]"
