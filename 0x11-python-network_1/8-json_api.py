#!/usr/bin/python3
"""
    this took in a letter and sends a POST request to http://0.0.0.0:5000/search_user
    q was rhe variable
    q="" was setted in case there is no args
    the id and name was displayed like this: [<id>] <name>
    Not a valid JSON incase the JSON is invalid
    No result incase the JSON is empty
    request and sys packaged was used 
    amd no other oackages was imppryed
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        r = requests.post(url, data={'q': argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        obj_js = r.json()
        if obj_js:
            print("[{}] {}".format(obj_js.get("id"), obj_js.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
