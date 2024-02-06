#!/usr/bin/python3
"""define function that creates object file from Json"""
import json

def load_from_json_file(filename):
    """fucntion that creates an Object from a "JSON file" """
    with open(filename) as myfile:
        return json.load(myfile)
