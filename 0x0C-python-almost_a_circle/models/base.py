#!/usr/bin/python3
""" 1st task """
import json
from sys import path


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON string representation """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        that writes the JSON string representation of list_objs
        """
        new_list = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open(file_name, 'w') as file:
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        - That returns an instance with all attributes already set
        - Create a `dummy` mandatory attr in Rectangle or Square instance
        - **dictionary must be used as **kwargs of the method update
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(0, 0)
        else:
            obj = cls(0)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ method returns a list of instances """
        filename = cls.__name__ + '.json'
        try:
            ...
        except:
            return []