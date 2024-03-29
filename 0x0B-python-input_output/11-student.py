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
    def to_json(self, attrs=None):
        """Get a dictionary represenation of the studnet"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

        def reload_from_json(self, json):
            """ replaces all attributes of the Student instance."""
            for k, v in json.items():
                setattr(self, k, v)
