#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    find the maximum value of a list
    Args:
        my_list - function of list to search.
    Return:
        None - function if list is empty.
        maximum of list
    """

    length = len(my_list)
    if length == 0:
        return None
    Max = my_list[0]
    for v in my_list:
        if v > Max:
            Max = v
    return Max
