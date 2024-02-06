#!/usr/bin/python3
"""define function read_file"""
def read_file(filename=""):
    """function that reads file and prints to stdout.

    Ags:
        filename: name of file to read"""
    with open(filename, encoding = "utf-8") as myfile:
        print(myfile.read())
