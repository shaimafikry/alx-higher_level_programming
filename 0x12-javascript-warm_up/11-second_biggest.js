#!/usr/bin/node
// get the second biggest number
const process = require('node:process');
function biggest (argv) {
  let m;
  let big = 0;
  let sBiggest = 0;
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
