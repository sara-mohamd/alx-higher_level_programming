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

    @property
    def size(self):
        """ get """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value

    def update(self, *args, **kwargs):
        """
        Update the rectangle
        1st arg (id)
        2nd arg (size)
        3rd arg (x)
        4th arg (y)
        "no-keyword argument"
        **kwargs must be skipped if *args exists and is not empty
        """
        if args:
            #       Don't forget pycodestyle
            for arg, attr in zip(args, ['id', 'size', 'x', 'y']):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Almost a Circle! """
        __dict = super().to_dictionary()
        __dict['size'] = __dict['width']
        del __dict["width"], __dict["height"]
        return __dict
        # _dict = {}
        # for key, val in self.__dict__.items():
        #     k = key.split('__')[-1]
        #     _dict[k] = val
        # return _dict
