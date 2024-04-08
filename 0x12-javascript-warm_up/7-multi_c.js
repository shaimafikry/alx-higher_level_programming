#!/usr/bin/node
// takes argument, prints string based on it
const process = require('node:process');
const x = +process.argv[2];
if (isNaN(x)) { console.log('Missing number of occurrences'); }
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}
