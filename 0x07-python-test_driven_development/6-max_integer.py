#!/usr/bin/python3
"""Module to find the max int in a list
"""


def max_integer(list=[]):
    """Funcs to find and return the max integ in a list of integ
        If the list is empty, the funct returns Noness.
    """
    if len(list) == 0:
        return None
    result = list[0]
    k = 1
    while k < len(list):
        if list[k] > result:
            result = list[k]
        k += 1
    return result
