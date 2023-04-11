#!/usr/bin/python3
"""Module for is_same_class()"""

def is_same_class(obj, a_class):
    """
    Return whether an object is an instance a class or not

    Args:
        obj: the object.
        a_class: the class.
    """
    return type(obj) is a_class
