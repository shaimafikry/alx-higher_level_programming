#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
// You must use the module request
const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');
// The first argument is the URL to request
const url = argv[2];
// The second argument the file path to store the body response
const fileName = argv[3];
request.get(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = response.body;
    fs.writeFileSync(fileName, data);
  }
});
