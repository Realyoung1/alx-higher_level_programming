#!/usr/bin/python3


def multiply_by_2(m_dict):
    """
    a func that returns a new dict with all values multiplied by 2
    """
    if m_dict is None:
        return None
    else:
        return {key: m_dict[key] * 2 for key in m_dict}
