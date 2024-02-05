#!/usr/bin/python3
"""defines class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """iniialise a rectangle using with width and height
        Args:
        width (int): width of new rectangle.
        height )int): height of new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
