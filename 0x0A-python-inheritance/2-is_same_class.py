#!/usr/bin/python3
"""Defining a class-checking functin."""


def is_same_class(obj, a_class):
    """Checks if an objt is exact as an instance of a given class.

    Args:
        obj (any): The objt to check.
        a_class (type): The class to match the type of objt to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
