#!/usr/bin/python3


def best_score(m_dict):
    """
    a func that returns a key with the biggest integers value.
    """
    if m_dict is None or m_dict == {}:
        return None
    for key in m_dict.keys():
        if m_dict[key] == max(m_dict.values()):
            return key
