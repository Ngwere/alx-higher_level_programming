#!/usr/bin/python3
"""
The lookup module

Module contain one function lookup().
"""


def lookup(obj):
    """
    return the list of attributes and methods

    Args:
        obj (obj): the object
    """
    return dir(obj)
