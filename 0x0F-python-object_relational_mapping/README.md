<h> Python - Object-relational mapping </h>

	db_connect = MySQLdb.connect => begins the connection
	cursor = db_connect.cursor() => begind th curser
	cursor.excute => hold the query orders
	query_rows = sql_order.fetchall() => holds all the data 
	cursor.close() => closes the cursor
	db_connect.close() => closes the connection

* We can use REGEX to search for specific names in sql tables :
	<div> SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC; </div>
