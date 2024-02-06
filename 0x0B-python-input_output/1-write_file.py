#!/usr/bin/python3
"""define function that writes string to a file"""

def write_file(filename="", text=""):
    """writes texts to a ext file (UTF8) and returns the number of characters written.

    Args:
    fiename: file that should contain content
    text: text to be written.
    """
    with open(filename, mode = 'w', encoding = "utf-8") as myfile:
        return myfile.write(text)
