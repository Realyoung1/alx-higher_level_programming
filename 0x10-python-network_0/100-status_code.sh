#!/bin/bash
# bash script that sends url, passed arg and not uses pipe, redi
curl -s -o /dev/null -I -w "%{http_code}" "$1"
