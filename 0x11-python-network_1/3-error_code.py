#!/usr/bin/python3
"""
    it takes URL, also sends a request to the URL which displayed the body
    urllib.error.HTTPError was managaed with Error code exceptions
    no other packages was imported
    each variable values are diffent to each request
    i didnt check any values
    with statement was used 
    it was rested on the sandbox
"""

from urllib import (request, parse, error)
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read()

        print(body.decode('utf8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
