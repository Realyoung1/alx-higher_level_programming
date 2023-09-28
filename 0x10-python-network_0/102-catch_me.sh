#!/bin/bash
# scripted that makes request, uses curl and refuesed echo, cat etc
curl -X PUT -L -H "Origin: HolbertonSchool" -s 0.0.0.0:5000/catch_me -d 'user_id=98'
