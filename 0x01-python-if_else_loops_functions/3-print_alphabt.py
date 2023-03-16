#!/usr/bin/python3
# 3-print_alphabt.py

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if letter != 'e' or 'q':
        print("{}".format(chr(letter)), end="")
