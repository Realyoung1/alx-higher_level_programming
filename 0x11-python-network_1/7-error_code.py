#!/usr/bin/python3
"""
    scripted which Takes in a URL, sends a request to the URL
    HTTP status code is greater than or equal to 400,
    ony requests and syss packages was used
    no other oackages was imported
    indidnt check for args
    it was then twsted on the sandbox
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if int(r.status_code) < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
