#!/usr/bin/node
const fs = require('fs');
// to obtain the path to the file you want to read from argument
const { argv } = require('process');

// define variables to hold data
let data1, data2, content;
try {
  // Use fs.readFileSync to read the file
  data1 = fs.readFileSync(argv[2], 'utf8');
  data2 = fs.readFileSync(argv[3], 'utf8');
  // add them together
  content = data1 + data2;
} catch (err) {
  console.error('An error occurred:', err);
}
// to write to a file
try {
  fs.writeFileSync(argv[4], content);
  // file written successfully
} catch (err) {
  console.error(err);
}
