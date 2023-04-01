#!/usr/bin/python3

def raise_exception_msg(message=""):
    n = "t"
    try:
        print(5 + n)
    except TypeError:
        print(message)
