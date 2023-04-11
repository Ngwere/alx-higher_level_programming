#!/usr/bin/python3
"""
The MyList module

Module contain one class Mylist.
"""


class MyList(list):
    """
    This class contains the print_sorted() method
    This function is inherited from list
    """
    def print_sorted(self):
        print(sorted(self))
