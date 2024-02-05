#!/usr/bin/python3
"""define a class with instance method"""
class BaseGeometry:
    """Class BaseGeometry with public instance method"""
    def area(self):
        """public instant method area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """public instant method that validates value.
        Args:
        name: string value.
        value: interger value.
        raises:
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer.
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0"""
        
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


