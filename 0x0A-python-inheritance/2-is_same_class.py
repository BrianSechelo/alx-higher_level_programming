#!/usr/bin/python3
"""define function is_same_class"""
def is_same_class(obj, a_class):
    """ fucntion that returns True if the object is exactly 
    an instance of the specified class ; otherwise False
    Args:
    obj (Any): The obejct to be checked.
    a_class(Type): The ckass to match the type of obj to.
    """
    if type(obj) == a_class:
        return True
    return False
