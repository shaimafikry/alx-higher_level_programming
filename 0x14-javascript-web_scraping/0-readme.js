#!/usr/bin/node
// Write a script that reads and prints the content of a file.
// import file module
const fs = require('fs');

// bring the argv
const { argv } = require('node:process');
const filename = argv[2];
// The content of the file must be read in utf-8
try {
  const data = fs.readFileSync(filename, 'utf-8');
  console.log(data);
// If an error occurred during the reading, print the error object
} catch (err) {
  console.log(err);
}
