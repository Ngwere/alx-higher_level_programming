#!/usr/bin/python3
"""Module for is_same_class

Contains the function that compaures object with class.
"""

def is_kind_of_class(obj, a_class):
    """
     Return true if object is instance of class or inherited from class
    """
    return isinstance(obj, a_class)
