#!/usr/bin/python3
"""
    X-Request-Id value was diplayed by this script, an also takes url, send request to url
    requests wnd sys packages was used
    each request varibke valies are different
    args was not checked
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
