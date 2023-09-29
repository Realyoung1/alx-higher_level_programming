#!/usr/bin/python3
"""
     I fetchesd https://alx-intranet.hbtn.io/status with this python script
     urllib package was used
     no other packages was imported
     the body of the response was diplayed
     i used the "with" statement
"""


from urllib import (request)
if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        body = response.read()
     
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf8')))
