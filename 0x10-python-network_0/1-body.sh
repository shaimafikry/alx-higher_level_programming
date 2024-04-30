#!/bin/bash
# script takes URL, sends Get request to URL, displays size of body of response
curl -sX GET "$1"
