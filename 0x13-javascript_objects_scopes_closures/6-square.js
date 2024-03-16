#!/usr/bin/node
const Square = require('./5-square');
class Square {
	charPrint(c) {

		if (c){
			for (let i = 0; i < this.height; i++){
				for (let m = 0; m < this.width; m++)
				{
					process.stdout.write(c);
				}
				console.log();
		  }

		}
		else {

			Square.print();
		}
	}
  }
  
  module.exports = Square;
  