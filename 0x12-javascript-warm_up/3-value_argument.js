#!/usr/bin/node
// print first argument
const { argv } = require('node:process');
if (!argv[2]) { console.log('No argument'); } else { console.log(argv[2]); }
