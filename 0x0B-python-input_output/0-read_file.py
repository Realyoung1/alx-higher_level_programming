#!/usr/bin/python3
"""
functions that reads a text files..
"""


def read_file(filename=""):
    """read the text file (UTF8) and prints it to stdout
    Returns nones.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
