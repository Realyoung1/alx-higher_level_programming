#!/usr/bin/python3
for k in range(ord("a"), ord("z") + 1):
    if chr(k) == "q" or chr(k) == "e":
        continue
    else:
        print("{:s}".format(chr(k)), end="")
