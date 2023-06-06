#!/usr/bin/python3
k = 122
while k >= 97:
    move = 0
    if k % 2 != 0:
        k = k - 32
        move = 1
    print("{:s}".format(chr(k)), end="")
    if move == 1:
        k = k + 32
    k = k - 1
