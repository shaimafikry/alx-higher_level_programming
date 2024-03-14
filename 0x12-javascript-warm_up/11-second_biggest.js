#!/usr/bin/node
const process = require('node:process');
function biggest (argv) {
  let m;
  let big = +argv[2];
  let sBiggest = +argv[2];
  for (m = 2; !(isNaN(+argv[m])); m++) {
    if (big <= +argv[m]) {
      big = +argv[m];
    }
  }
  for (m = 2; !(isNaN(+argv[m])); m++) {
    if (sBiggest <= +argv[m]) {
      if (+argv[m] < big) {
        sBiggest = +argv[m];
      }
    }
  }
  return sBiggest;
}
if (process.argv.length <= 3) { console.log('0'); } else { console.log(biggest(process.argv)); }
