#!/usr/bin/node
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
