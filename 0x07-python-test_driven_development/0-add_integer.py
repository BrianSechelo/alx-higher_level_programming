#!/usr/bin/python3
"""Defines an interger addition function"""

def add_integer(a, b=98):
    """Returns the interger addition of a and b.
    Float values are typecasted to int before addition.
    Raises:
        TypeError: if either of a or b is a non-interger and non-float.
        """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integerr")
    if ((not isinstance(b, int) and not isinstance(b, float))):
         raise TypeError("b must be an integerr")
    return (int(a) + int(b))

