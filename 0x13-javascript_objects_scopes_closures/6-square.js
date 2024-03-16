#!/usr/bin/node
const Square = require('./5-square');
class Square extends Square{
	charPrint(c) {

		if (c){
			for (let i = 0; i < this.height; i++) {
				console.log(c.repeat(size));
		  }
		}
		else {
			Square.print();
		}
	}
  }
  
  module.exports = Square;
  