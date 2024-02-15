#!/usr/bin/python3
""" Task 9 """


class Student:
    """ Class define a student """

    def __init__(self, first_name, last_name, age):
        """ Initializing method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list)
                and all(isinstance(var, str) for var in attrs)):
            return {key: getattr(self, key) for key in
                    attrs if hasattr(self, key)}

        return self.__dict__
