#!/usr/bin/python3
"""define a class student"""
class Student:
    """class that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """ get a dictionary representation of the student."""
        return self.__dict__
