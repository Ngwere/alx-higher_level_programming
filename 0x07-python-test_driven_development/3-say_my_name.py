#!/usr/bin/python3
"""
This is the module for say_my_name.

This module contains one function say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first_name> <last_name>

    Args:
        first_name (str) - the first name
        last_name (str) - the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
