#!/usr/bin/python3
"define fucntion that writes an object to a text file"""
import json

def save_to_json_file(my_obj, filename):
    """write an object to a textfile using python representation."""
    with open(filename, mode="w") as myfile:
        json.dump(my_obj, myfile)
