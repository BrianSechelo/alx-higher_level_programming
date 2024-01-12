#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmpp = a_dictionary.copy()
    for i, j in tmpp.items():
        if value == j:
            a_dictionary.pop(i)
    return a_dictionary


