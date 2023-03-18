#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = set(my_list)
    rest = 0
    for item in result:
        rest += item
    return rest
