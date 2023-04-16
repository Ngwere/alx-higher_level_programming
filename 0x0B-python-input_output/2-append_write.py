#!/usr/bin/python3
"""read_line module with read_line() function"""


def write_file(filename="", text=""):
    """
    read lines and return the number of characters

    Args:
        filename (str) - the filename of the file to be read
        text (str) - the number of lines to be read
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
