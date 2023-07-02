#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Printss a square with the # characterss.
    Args:
        size (int): this is The height/width of the squaress.
    Raises:
        TypeError: If size is not an intss.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        [print("#", end="") for d in range(size)]
        print("")
