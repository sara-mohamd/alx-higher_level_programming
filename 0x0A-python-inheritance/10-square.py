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

    def area(self):
        """ Calc Area """
        return (self.__size ** 2)
