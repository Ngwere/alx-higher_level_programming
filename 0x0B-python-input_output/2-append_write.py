#!/usr/bin/python3
"""read_line module with read_line() function"""


def append_write(filename="", text=""):
    """
    read and append lines to a file

    Args:
        filename (str) - the filename of the file to be read
        text (str) - the number of lines to be read
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
