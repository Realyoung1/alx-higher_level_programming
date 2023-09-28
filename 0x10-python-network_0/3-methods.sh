#!/bin/bash
# bash scripted that displayed http and uses urls
curl -sI -X OPTIONS "$1" | grep -i Allow | cut --complement -d ' ' -f 1
