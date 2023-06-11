#!/usr/bin/python3
def new_in_list(my_list, vdx, element):
    """
    replace an element from a list at index vdx with element
    Args:
        my_list - function list to search.
        vdx - function the position to access.
        element - new element to swap with.
    Return:
        modified my_list
    """

    copy_list = my_list[:]
    if vdx < 0 or vdx >= len(copy_list):
        return copy_list
    copy_list[vdx] = element
    return copy_list
