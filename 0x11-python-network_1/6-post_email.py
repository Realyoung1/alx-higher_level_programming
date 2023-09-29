#!/usr/bin/python3
"""
    it taked in a URL, the email and sends a POST request
    email was sent kn the variable emails
    onky requesta and sys pckahes was used
    args erroe was not checked
    it was tested in the sandbox
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
