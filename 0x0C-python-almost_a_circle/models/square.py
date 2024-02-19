#!/usr/bin/python3
""" Task 10 """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    it's already Almost a Circle !
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(width=size, height=size, x=x, y=y, id=id)


    def __str__(self):
        """ str representation """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"