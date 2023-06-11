#!/usr/bin/python3

def replace_in_list(my_list, vdx, element):
    """
    replaces an elment from a list at index vdx with element
    Args:
        my_list - function list to search.
        vdx - function the position to access.
        element - new elem to swap with
    Return:
        my_list
    """

    if vdx < 0 or vdx >= len(my_list):
        return my_list
    my_list[vdx] = element
    return my_list
