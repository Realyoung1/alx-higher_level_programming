#!/usr/bin/python3
"""
    scripted which took my Github credentials (username and password)
    basic authenticator and personak acces token was hsed 
    my user name was the first arg
    my secojd args was my PAT
    requests and sys oackahe was useed 
    no other oackage was imported
    no args was checked
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, passw))
    print(r.json().get("id"))
