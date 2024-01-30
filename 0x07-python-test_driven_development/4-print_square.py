#!/usr/bin/python3
"""Define a print square function"""
def print_square(size):
    """ prints a square with the character #.
    Args:
            size: length of square.
    Raises: TypeError:if size is not interger
          : ValueError: if size is less than 0  
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
