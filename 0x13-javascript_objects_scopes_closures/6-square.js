#!/usr/bin/node
// extends from class and use its methods
// trying c.repeat instead of process.stdout
const baseSquare = require('./5-square');
class Square extends baseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
