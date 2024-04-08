#!/usr/bin/node
// exports function that has a function
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) { theFunction(); i++; }
};
