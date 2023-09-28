#!/usr/bin/python3
"""
    find_peak test function
"""

def find_peak(list_of_integers):
    """Finded peak in the list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    g = len(list_of_integers) - 1
    f = 0
    lis = list_of_integers
    while g > f:
        half = (g + f) // 2
        if lis[half] <= lis[half + 1]:
            f = half + f
        elif lis[half] <= lis[half - 1]:
            g = half - f
        elif lis[half] >= lis[half + 1] and lis[half] >= lis[half - 1]:
            return lis[half]
    return lis[f]
