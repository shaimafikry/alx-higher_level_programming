#!/usr/bin/node
const process = require('node:process');
function add (a, b) {
  const result = a + b;
  return result;
}
const a = +process.argv[2];
const b = +process.argv[3];

console.log(add(a, b));
