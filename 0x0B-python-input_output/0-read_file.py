#!/usr/bin/python3
"""the read_file module that contains the read_file() function"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
