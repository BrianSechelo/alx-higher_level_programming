#!/usr/bin/python3
"""Defines an object attribute to lookup fyunction"""

def lookup(obj):
    """Returns a lsit of an object's available attributes"""
    return (dir(obj))
