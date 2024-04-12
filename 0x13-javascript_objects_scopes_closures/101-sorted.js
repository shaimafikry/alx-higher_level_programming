#!/usr/bin/node
// script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;

const numOfId = {};
let key, value;
for ([key, value] of Object.entries(dict)) {
  const strValue = value.toString();
  if (numOfId[strValue]) {
    numOfId[strValue].push(key);
  } else {
    numOfId[strValue] = [key];
  }
}

console.log(numOfId);
