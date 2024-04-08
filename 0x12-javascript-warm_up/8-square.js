#!/usr/bin/node
// represent strings as x in shape of square
const process = require('node:process');
const x = +process.argv[2];
if (isNaN(x)) { console.log('Missing size'); }
let i = 0;
let m = 0;
while (i < x) {
  while (m < x) {
    process.stdout.write('X');
    m++;
  }
  process.stdout.write('\n');
  i++;
  m = 0;
}
