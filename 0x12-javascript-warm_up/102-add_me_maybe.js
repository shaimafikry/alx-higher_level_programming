#!/usr/bin/node
// exports a function that add a number before printing it
exports.addMeMaybe = function (number, theFunction) { theFunction(++number); };
