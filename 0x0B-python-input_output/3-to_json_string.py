#!/usr/bin/python3
"""Module contains to_json_string(my_obj) function"""

import json


def to_json_string(my_obj):
    """the to_json_string function that return a json object

    Args:
        my_obj (obj) - the object
    """

    return json.dumps(my_obj)
