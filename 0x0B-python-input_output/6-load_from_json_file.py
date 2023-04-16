#!/usr/bin/python3
"""load_from_json_file module withe the load_from_json() function"""


import json


def load_from_json_file(filename):
    """ load from json file

    Args:
        filename () - the file name
    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
