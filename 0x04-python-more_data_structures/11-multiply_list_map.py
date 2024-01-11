#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def mul_no(num):
        return num * number
    return list(map(mul_no, my_list))
