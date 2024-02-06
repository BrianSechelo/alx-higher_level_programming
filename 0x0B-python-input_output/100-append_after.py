#!/usr/bin/python3
"""define a function that inserts text to a file."""
def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string.
    
    Args:
    filename (str): The name of the file. 
    search_string (str): The string to search for within the file.
    new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as n:
        n.write(text)
