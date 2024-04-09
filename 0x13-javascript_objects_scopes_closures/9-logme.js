#!/usr/bin/node
// concept of global variable
global.num = 0;
exports.logMe = function (item) {
  console.log(global.num++ + ': ' + item);
};
