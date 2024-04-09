#!/usr/bin/node
// define a class square that inherts from rectangla class
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }
}

module.exports = Square;
