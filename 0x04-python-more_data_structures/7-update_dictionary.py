#!/usr/bin/python3


def update_dictionary(m_dict, key, value):
    """
    add or replace a new key value in dict
    """
    if m_dict is None:
        return None
    m_dict[key] = value
    return m_dict
