#!/usr/bin/python3
"""define a class that inherits form class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Class square that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        """initialise a new square.
        Args:
        size (int): size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
