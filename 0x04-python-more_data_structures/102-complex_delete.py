#!/usr/bin/python3


def complex_delete(m_dict, value):
    """
    removes a value in a dictiinaries
    """
    if m_dict is None:
        return None
    delete_key = None
    keys = tuple(m_dict.keys())
    for key in keys:
        if m_dict[key] == value:
            del m_dict[key]
    return m_dict
