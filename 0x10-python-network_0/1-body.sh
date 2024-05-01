#!/bin/bash
# script takes URL, sends Get request to URL, displays CONTENT ONLY 200 of body of response
curl -sL "$1"
