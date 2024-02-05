#!/usr/bin/python3
"""define My class list"""

class MyList(list):
    """MyList class that inherists from list"""

    def print_sorted(self):
        """Public instantce method that prints sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)

