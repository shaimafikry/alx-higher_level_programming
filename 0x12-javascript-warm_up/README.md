java script 
loading ...
* how to get the process  and command line?
	using  require ('node: process')
	if process used as a variable , you would get thewhole process data (including pid ppid ...etc)
* how to access the command line ?
	 argv = process.argv .. 
* how to make it one step ?
	by using the distructuring assigment syntax
	const {argv } = require (node: process)
	