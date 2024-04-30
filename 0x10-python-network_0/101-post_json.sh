#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "$2" -H "Content-Type: application/json" "$1"
