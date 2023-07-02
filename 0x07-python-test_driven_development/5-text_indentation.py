#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Printss texts with two new lines after each '.', '?', and ':'.
    Args:
        text (string): this is The text to printss.
    Raises:
        TypeError: If texts is not a stringss.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
