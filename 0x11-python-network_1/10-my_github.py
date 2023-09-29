#!/usr/bin/python3
"""
    this took my Github credentials (username and password)
    Basic Authentication with a PAT was used as password
    username is the first arg
    password is the second arg
    requests and sys packages ess used
    no other packages was imported
    no args was checked
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, passw))
    print(r.json().get("id"))
