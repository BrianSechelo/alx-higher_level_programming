#!/usr/bin/python3
"""define a function append_write"""

def append_write(filename="", text=""):

    """function that appends text to file.

    Args:
    filename: name of file
    text: text to be appended to file
    
    Returns: number of characters added.
        """
    with open(filename, mode="a", encoding="utf-8") as myfile:
           return myfile.write(text)

