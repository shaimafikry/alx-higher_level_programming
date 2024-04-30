#!/bin/bash
# script takes URL, sends Get request to URL, displays size of body of response
curl -sXH GET "X-School-User-Id: 98" "$1"
