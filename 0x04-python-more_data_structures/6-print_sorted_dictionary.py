#!/usr/bin/python3


def print_sorted_dictionary(m_dict):
    """
    print a dicts in sorted order of key.
    """
    if m_dict is None:
        return None
    for key in sorted(m_dict.keys()):
        print("{:s}: {}".format(key, m_dict[key]))
