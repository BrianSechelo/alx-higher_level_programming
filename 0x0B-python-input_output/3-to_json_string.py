#!/usr/bin/python3
"""define a string to Json function"""
import json
def to_json_string(my_obj):
    """Return the json representation of a string object."""
    return json.dumps(my_obj)
