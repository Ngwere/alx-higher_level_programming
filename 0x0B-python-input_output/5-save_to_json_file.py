#!/usr/bin/python3
"""the save_to_json_file module withe the save_to_file() function"""


import json


def save_to_json_file(my_obj, filename):
    """the save_to_json_file function write object to text file

    Args:
        my_obj (str) - the object
        file_name (str) - the file name
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
