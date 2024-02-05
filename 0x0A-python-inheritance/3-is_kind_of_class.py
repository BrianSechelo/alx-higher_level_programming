#!/usr/bin/python3
"""define a fucntion is_kind_of_class"""
def is_kind_of_class(obj, a_class):
    """function that check if the object is an instance of,
    or if the object is an instance of a class that inherited from, the specified class.

    Args:
    obj(any): object to be checked.
    a_class(Type): Base class or subb-class to contain obj.

    return:
    True:if object is an instance of base of sub class.
    False: if otherwise"""

    if isinstance(obj, a_class):
        return True
    return False
