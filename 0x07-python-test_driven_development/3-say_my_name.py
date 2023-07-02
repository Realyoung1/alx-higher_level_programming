#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a namess.
    Args:
        first_name (str): this is The first namess to prints.
        last_name (str): this is The last namess to prints.
    Raises:
        TypeError: If either of first_name or last_name are not stringss.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
