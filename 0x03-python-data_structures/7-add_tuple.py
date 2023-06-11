#!/usr/bin/python3

def add_tuple(a=(), b=()):
    """
    add the firsst and second elemens of a b
    if any of a or b is less than 2 elemens
    0 is padded.
    Args:
        a - funtion for tuple default empty
        b - function for tuple default empty
    Return:
        (c, d)
    """
    while len(a) < 2:
        a = (*a, 0)
    while len(b) < 2:
        b = (*b, 0)
    return a[0] + b[0], a[1] + b[1]
