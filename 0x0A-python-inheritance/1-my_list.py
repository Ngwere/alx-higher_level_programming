#!/usr/bin/python3
"""
The MyList module

Module contain one class Mylist.
"""


class MyList(list):
    """
    This function is inherited from list
    """

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
