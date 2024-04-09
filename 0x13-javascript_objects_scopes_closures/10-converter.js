#!/usr/bin/node
// apply the concept of Higher-order functions
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
