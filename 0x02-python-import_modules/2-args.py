#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    argc = len(args)
    first_line = "{:d} argument".format(argc)
    if argc == 0:
        first_line += "s."
    elif argc == 1:
        first_line += ":"
    else:
        first_line += "s:"
    print(first_line)
    for V, _arg in enumerate(args):
        print("{:d}: {:s}".format(V+1, _arg))
