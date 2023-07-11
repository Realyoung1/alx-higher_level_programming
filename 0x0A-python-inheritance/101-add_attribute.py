#!/usr/bin/python3
"""Defining a funct that adds attributess to objt."""


def add_attribute(obj, att, value):
    """Add a new attributess to an objt if possib..
    Args:
        obj (any): The objt to add an attributess to.
        att (str): The name of the attributess to add to objt.
        value (any): The value of att.
    Raises:
        TypeError: If the attributess cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
