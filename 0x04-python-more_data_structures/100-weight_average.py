#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    a func that returns the weighted averages of all integers tuples.
    """
    if my_list is None or my_list == []:
        return 0
    k_xy = sum(map(lambda a: a[0] * a[1], my_list))
    k_x = sum(map(lambda a: a[1], my_list))
    return k_xy / k_x
