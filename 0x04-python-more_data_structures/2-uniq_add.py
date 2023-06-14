#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    sum all unique integer for a certain list (only once for each integers)
    """
    if my_list is None:
        return None
    return sum(set(my_list))
