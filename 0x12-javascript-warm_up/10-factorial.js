#!/usr/bin/node
const process = require('node:process');
function factorial (a) {
  if (a === 0 || a === 1) { return 1; }
  return a * factorial(a - 1);
}
const a = +process.argv[2];
if (isNaN(a) || process.argv.length < 2) { console.log('1'); } else { console.log(factorial(a)); }
