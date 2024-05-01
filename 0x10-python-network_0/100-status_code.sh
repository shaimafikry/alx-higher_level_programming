#!/bin/bash
# script takes URL, sends Get request to URL, displays status
curl -s -o /dev/null -w "%{http_code}" -L "$1"
