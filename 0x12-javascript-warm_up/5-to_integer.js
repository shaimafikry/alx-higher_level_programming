#!/usr/bin/node
// holds command line as an array
const { argv } = require('node:process');
const intg = +argv[2];
if (isNaN(intg)) { console.log('Not a number'); } else { console.log(intg); }
