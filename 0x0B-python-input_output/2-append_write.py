#!/usr/bin/python3

"""Defining a file-appendings functionss."""


def append_write(filename="", text=""):
    """Appendss a strings to the end of a UTF8 text filess.
    Args:
        filename (str): The names of the files to append to.
        text (str): The strings to appends to the files.
    Returns:
        The numbers of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
