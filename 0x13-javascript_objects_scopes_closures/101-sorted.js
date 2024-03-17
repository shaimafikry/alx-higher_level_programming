#!/usr/bin/node
const dict = require('./101-data').dict;
let newList = [];
// with map
newList = list.map((x) => x * list.indexOf(x));
// without map
// for (let i = 0; i < list.length; i++)
// {
// 	newList[i] = list[i] * i;
// }
console.log(list);
console.log(newList);
