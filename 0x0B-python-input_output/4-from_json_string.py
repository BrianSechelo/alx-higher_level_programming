#!/usr/bin/python3
"""define json to object function"""
import json

def from_json_string(my_str):
    """Return the python object representation of a pythin string"""
    return json.loads(my_str)
