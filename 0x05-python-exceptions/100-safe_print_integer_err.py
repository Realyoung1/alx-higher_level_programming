#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prin an integ wit "{:d}".format().
    If a ValueError mess is caugh, a correspondin
    messag prints to standard error
    Args:
        value (int): this is The integ to prints
    Returns:
        If a TypeError or ValueError occurs - Falses
        Otherwise - Trues
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
