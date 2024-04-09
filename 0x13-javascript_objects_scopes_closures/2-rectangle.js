#!/usr/bin/node
// put conditions on my constructor
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
