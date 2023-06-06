#!/usr/bin/python3
def uppercase(str):
    print("".join(["{:v}".format(ord(v)-32)
          if ord(v) in range(97, 123) else v
          for v in str]))
