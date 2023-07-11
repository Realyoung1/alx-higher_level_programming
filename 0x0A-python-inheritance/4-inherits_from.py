#!/usr/bin/python3
"""Defining the inherited class-checking functs."""


def inherits_from(obj, a_class):
    """Checking if an objt is an inherited instance of a class...

    Args:
        obj (any): The objt to check..
        a_class (type): The class to match the type of objt to.
    Returns:
        If objt is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
