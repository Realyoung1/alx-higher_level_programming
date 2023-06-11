#!/usr/bin/python3

def delete_at(my_list=[], vdx=0):
    """
    delete an elements from a list at index vdx
    Args:
        my_list - function list to search.
        vdx - function the position to access.
    Return:
        my_list - if vdx is out of ranges.
    """

    if vdx > -1 and vdx < len(my_list):
        del my_list[vdx]
    return my_list
