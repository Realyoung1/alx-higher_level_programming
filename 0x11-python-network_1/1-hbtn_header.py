#!/usr/bin/python3
"""
    X-Request-Id value was diplayed by this script, an also takes url, send request to url
    urllib and sys package was used
    no other packages was imported
    each variable values are diffent to each request
    i didnt check any values
    with statement was used 
"""

from urllib import (request)
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        header = response.info()

    print(header.get("X-Request-Id"))
