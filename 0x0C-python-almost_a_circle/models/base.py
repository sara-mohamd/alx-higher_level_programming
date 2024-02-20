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
        if list_objs is None:
            with open(file_name, 'w') as file:
                file.write(json.dump(list_objs))
        #     with open(file_name, 'w') as file:
        #     return
        for i in list_objs:
            new_list.append(i.to_dictionary())
        with open(file_name, 'w') as file:
            file.write(cls.to_json_string(new_list))
