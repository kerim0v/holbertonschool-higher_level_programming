#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print("{}".format(a / b))
        return (a / b)
    except ZeroDivisionError:
        return None
