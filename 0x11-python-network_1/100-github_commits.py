#!/usr/bin/python3
"""
    python scripted tyat takes two args
    repository name is the 1st arg
    owner name is the 2nd arg
    requests and sys oackahe was useed 
    no other oackage was imported
    no args was checked
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(user, repo)
    url += '/commits?per_page=10'
    r = requests.get(url)
    for c in r.json():
        print("{}: {}".format(c.get("sha"
                                    ), c.get("commit"
                                             ).get("author"
                                                   ).get("name")))
