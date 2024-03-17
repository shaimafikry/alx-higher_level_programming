#!/usr/bin/node
const list = require('./100-data').list;
let newList = [];
// with map
newList = list.map((x, index) => x * index);
// without map
// for (let i = 0; i < list.length; i++)
// {
// newList[i] = list[i] * i;
// }
console.log(list);
console.log(newList);
