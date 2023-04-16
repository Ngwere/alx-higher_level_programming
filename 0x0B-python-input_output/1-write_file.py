#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    the write file function

    Args:
        filename (str) - the file name to be read
        text (str) - the lines to be read to file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
