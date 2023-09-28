#!/bin/bash
# bash script which displayed body of a 200 status code and used curl
curl -s -X GET -L "$1"
