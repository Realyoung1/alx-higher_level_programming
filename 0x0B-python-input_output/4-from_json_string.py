#!/usr/bin/python3

"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returning a the Python object representations of a JSON strings."""
    return json.loads(my_str)
