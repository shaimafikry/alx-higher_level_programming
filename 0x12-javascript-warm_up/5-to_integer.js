#!/usr/bin/node
// turns string into integer
const { argv } = require('node:process');
const intg = +argv[2];
if (isNaN(intg)) { console.log('Not a number'); } else { console.log('My number: ' + intg); }
