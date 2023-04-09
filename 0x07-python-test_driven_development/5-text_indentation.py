#!/usr/bin/python3
"""
The text_indentation module.

This module contains one function text_indentation().
"""
def text_indentation(text):
    """
    print text

    Args:
        text (str) - the text that is printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
