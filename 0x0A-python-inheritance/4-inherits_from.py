#!/usr/bin/python3
"""define function that checksobject instance"""
def inherits_from(obj, a_class):
    """function that checks if instance of object is of subclass
    Args: 
    obj (any): object to be checked.
    a_class: class to conatin instacne of object.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
    
