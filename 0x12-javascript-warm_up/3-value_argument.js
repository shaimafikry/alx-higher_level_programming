#!/usr/bin/node
// holds command line as an array
const { argv } = require('node:process');
if (!argv[2]) { console.log('No argument'); } else { console.log(argv[2]); }
