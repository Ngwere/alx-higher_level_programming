#!/usr/bin/python3
"""the append_write module with the append_write() function"""


import json


def from_json_string(my_str):
    """The from _json_string function returns the json of string

    Args:
        my_str (str) - the string
    """
    return json.loads(my_str)

