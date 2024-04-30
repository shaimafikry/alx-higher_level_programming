#!/bin/bash
# script takes URL, sends request to URL, displays size of body of response
curl -sI "$1"  | grep -i "Content-Length" | awk '{print $2}'
