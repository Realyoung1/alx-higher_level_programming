#!/usr/bin/python3
def uppercase(str):
    print("".join(["{:c}".format(ord(c)-32)
          if ord(c) in range(97, 123) else v
          for v in str]))
