#!/bin/bash
# scrited which set json, must send a post and uses curl
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
