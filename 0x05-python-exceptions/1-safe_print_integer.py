#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integ wit "{:d}".format().
    Args:
        value (int): This is the integ to prints
    Returns:
        If a TypeError or ValueError occurs - Falses.
        Otherwise - Trues.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
