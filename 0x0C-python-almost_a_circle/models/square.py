#!/usr/bin/python3
"""define class Square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """class square that inherits from class Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize class variables.
        Args:
            size (int): size of square
            x (int): x coordinate
            y (int): y coordinate
            id (int): identit of new square
            """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """get/set size."""
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update class.
        Args:
            *args (int): New attribute values
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs (dict):New key/value pairs of attribues.
            """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
        }

