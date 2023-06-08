#!/usr/bin/python3

import hidden_4 as h


def discover():
    name = dir(h)
    for V in name:
        if V[:2] != '__':
            print("{:s}".format(V))


if __name__ == "__main__":
    discover()
