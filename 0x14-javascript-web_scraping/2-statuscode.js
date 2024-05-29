#!/usr/bin/node
// Write a script that display the status code of a GET request.
const request = require('request');
// IMPORT THE ARGV
const { argv } = require('node:process');
// The first argument is the URL to request (GET)
const url = argv[2];
// get the status
request.get(url).on('response', function (response) { console.log(`code: ${response.statusCode}`); });
// The status code must be printed like this: code: <status code>
