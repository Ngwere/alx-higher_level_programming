#!/usr/bin/python3
"""read_line module with read_line() function"""


def read_lines(filename="", nb_lines=0):
    with open(filename, "r", encoding="UTF-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for index in range(nb_lines):
            print(f.readline(), end="")
