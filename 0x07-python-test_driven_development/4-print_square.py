#!/usr/bin/python3
"""
The def print_square module.

The module contains one function print_square().
"""
def print_square(size):
    """
    Print a square with #

    Args:
        size (str) - the size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print(#)

