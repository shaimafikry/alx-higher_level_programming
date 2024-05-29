#!/usr/bin/node
// Write a script that writes a string to a file.
// imort the fs module
const fs = require('fs');
// import the argv
const { argv } = require('node:process');
// The first argument is the file path
const filenamePath = argv[2];
// The second argument is the string to write
const content = argv[3];
// write to file
try {
  fs.writeFileSync(filenamePath, content);
  // If an error occurred during while writing, print the error object
} catch (err) {
  console.log(err);
}
