#!/usr/bin/python3
""" Q8 """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherates from BaseGeometry """

    def __init__(self, width, height):
        """ Initializing method """
        super().__init__()

        super().integer_validator('width', width)
        self.__width = width

        super().integer_validator('height', height)
        self.__height = height
