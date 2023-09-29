#!/usr/bin/python3
"""
    I Fetcheesd https://alx-intranet.hbtn.io/status with these oython script
    "requests" packahe was used
    no other packages was imported
    the examples given was used to displayed the bodu of the response
"""

import requests

if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
