<h> Python - Object-relational mapping </h>

	db_connect = MySQLdb.connect => begins the connection
	cursor = db_connect.cursor() => begind th curser
	cursor.excute => hold the query orders
	query_rows = sql_order.fetchall() => holds all the data 
	cursor.close() => closes the cursor
	db_connect.close() => closes the connection
<h>
* We can use Wild card to search for specific names in sql tables :<h>
	<div> SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC; </div>
	or with using regex
	<div> SELECT * FROM states WHERE name LIKE '^N' OR '^n' ORDER BY states.id ASC; </div>

* when you call a variable in sql command , you put (%s) and add in tuple form (state_name, )
	sql_order.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;",(state_name,))
