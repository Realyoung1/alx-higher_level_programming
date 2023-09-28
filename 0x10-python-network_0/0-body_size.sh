#!/bin/bash
# the bash scripted that displedyed sizes in bytes and uses curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
