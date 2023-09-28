#!/bin/bash
# bash scripted that taked ar as an arg, with header variable X-School-User-Id
curl -s -X GET -L -H "X-School-User-Id: 98" "$1"
