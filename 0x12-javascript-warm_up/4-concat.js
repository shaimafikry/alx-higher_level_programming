#!/usr/bin/node
// prints second and third argument
const { argv } = require('node:process');
console.log(argv[2] + ' is ' + argv[3]);
