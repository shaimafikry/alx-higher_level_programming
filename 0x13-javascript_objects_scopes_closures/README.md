welcome class in java script
code notes:
*things i learned while codind:
	c.repeat(n): print the c,  n times as like (print(c) * n)
	we can use it in console.log(c.rpeat(n)) to print multiple timesin one line before \n
**note:
in (10-main.js) : he defined a variable myConverter  = converter (base) and then used it as a function,  myConverter(3)
	so to solve this we used double return!
	function that returns  the result of tostring(base) and a function that holds this reult and return it to the printer see (10converter.js)
	''' javascript
	 exports.converter = function (base) {
 	 return  function (num) {
  	 return num.toString(base); }
		};
 '''
	""" This is a common pattern in JavaScript for creating higher-order functions, where a function returns another function."""
