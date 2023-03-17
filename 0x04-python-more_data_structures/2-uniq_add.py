#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    function to add unique integers in a list

    @Arg:
        my_list - list 
        """
    result = set(my_list)
    return sum(result)
