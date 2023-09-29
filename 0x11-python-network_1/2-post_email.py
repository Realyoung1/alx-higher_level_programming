#!/usr/bin/python3
"""
    URL was taken and an email, sends a POST request
    the email was set tk the email variable
    no other oackages was imported other than urllib and sys
    i didnt check any values
    with statement was used 
"""

from urllib import (request, parse)
from sys import argv

if __name__ == "__main__":
    values = {}
    values["email"] = argv[2]
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
