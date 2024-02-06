#!/usr/bin/python3
""" Q10 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Another Shape class """

    def __init__(self, size):
        """ Initializing method """
        super().__init__(size, size)

        super().integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """ String """
        return f"[Square] {self.__size}/{self.__size}"
