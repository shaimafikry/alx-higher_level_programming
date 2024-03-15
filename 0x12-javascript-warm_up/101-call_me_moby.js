#!/usr/bin/node
callMeMoby = function (x, theFunction){
let i = 0;
while (i < x) {
  theFunction();
  i++;
}