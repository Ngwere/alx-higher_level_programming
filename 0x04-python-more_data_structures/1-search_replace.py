#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Function that replaces search with replace from 
    my_list

    @Arg:
        my_list - is the list
        search - element to be replaced
        replace - new element
        """
    my_list = [replace if i == search else i for i in my_list]
    return my_list
