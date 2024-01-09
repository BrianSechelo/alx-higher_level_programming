#!/usr/bin/python3
def no_c(my_string):
    for j in my_string:
        if (j == "c") or (j == "C"):
            my_string = my_string[:my_string.index(j)] \
                    + my_string[my_string.index(j) + 1:]

    return my_string
