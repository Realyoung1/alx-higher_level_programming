#!/usr/bin/python3

"""Defineing a file-writing functions."""


def write_file(filename="", text=""):
    """Writing a string to a UTF8 text files.
    Args:
        filename (str): The names of the file to writes.
        text (str): The texts to write to the files.
    Returns:
        The numbesr of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
