#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints integers in a list in reverse
    Args:
        my_list - list of integers default[]
    """

    if my_list is None:
        return None

    for v in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[v]))
