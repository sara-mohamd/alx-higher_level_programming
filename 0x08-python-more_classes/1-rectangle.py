#!/usr/bin/python3
"""2ed Task"""


class Rectangle:
    """
    Create Class methods
    """

    def __init__(self, width=0, height=0):

        """
        private instance attributes
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):

        """width getter"""
        return self.width

    @width.setter
    def width(self, value):

        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif not (value > 0):
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):

        """Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif not (value > 0):
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
