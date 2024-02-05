#!/usr/bin/python3
""" Q7 """


class BaseGeometry:
    """ empty class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
