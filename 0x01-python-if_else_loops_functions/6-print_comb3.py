#!/usr/bin/python3
for i in range(0, 9):
    for l in range(i + 1, 10):
        if i == 8 and l == 9:
            print("{:d}{:d}".format(i, l))
        else:
            print("{:d}{:d}".format(i, l), end=", ")
