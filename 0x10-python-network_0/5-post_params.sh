#!/bin/bash
# script bahs url and send post, a variable email, subject and uses curl
curl -s -X POST -L "$1" -d 'email=test@gmail.com&subject=I will always be here for PLD'
