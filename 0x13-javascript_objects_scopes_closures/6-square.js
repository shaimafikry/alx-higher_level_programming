#!/usr/bin/node
const baseSquare = require('./5-square');
class Square extends baseSquare{
	charPrint(c) {
		if (c){
			for (let i = 0; i < this.height; i++) {
				console.log(c.repeat(this.height)); }
		}
		else {
			baseSquare.print();	}
	}
  }
  module.exports = Square;
  