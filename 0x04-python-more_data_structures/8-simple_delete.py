#!/usr/bin/python3


def simple_delete(m_dict, key=""):
    """
    a func that deletes a key in a dict.
    """
    if m_dict is None:
        return None
    if key in a_dict:
        del m_dict[key]
    return m_dict
