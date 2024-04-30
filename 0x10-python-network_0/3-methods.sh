#!/bin/bash
# script takes URL, takes in a URL and displays all HTTP methods
curl -sX OPTIONS "$1" HTTP/1.1 | grep Allow | awk (print $2)
