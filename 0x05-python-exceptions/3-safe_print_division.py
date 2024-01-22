#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        quotn = a / b
    except (TypeError, ZeroDivisionError):
        quotn = None
    finally:
        print("Inside result: {}".format(quotn))
    return (quotn)

