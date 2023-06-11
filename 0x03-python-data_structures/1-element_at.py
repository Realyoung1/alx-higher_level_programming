#!/usr/bin/python3

def element_at(my_list, vdx):
    """
    gets an elment from a list at index vdx
    Args:
        my_list - function list to search.
        vdx - function the position to access.
    Return:
        None - if vdx is out of ranges.
        Data - element at vdx.
    """

    if vdx < 0 or vdx >= len(my_list):
        return None
    else:
        return my_list[vdx]
