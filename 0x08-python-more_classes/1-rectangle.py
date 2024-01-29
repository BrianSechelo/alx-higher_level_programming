#!/usr/bin/python3
"""Define a rectangle class"""

class Rectangle:
    """Represent a Reftangle"""
    def __init__(self, width = 0, height = 0):
        """Initialise a new Reftangle.
        Args:
        width (int): the width of a new rectangle
        height (int): the height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of a rectangle"""
        return (self._width)
    @width.setter
    def width(self, value):
        """set the with of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    @property
    def height(self):
        """get/set the height of a rectangle"""
        return (self._height)
    @height.setter
    def height(self, value):
        """set the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

