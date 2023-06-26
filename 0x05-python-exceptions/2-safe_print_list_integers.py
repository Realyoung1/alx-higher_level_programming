#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end='')
            a += 1
        except (ValueError, TypeError):
            pass
    print()
    return a
