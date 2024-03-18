<h> Python - Object-relational mapping </h>

	db_connect = MySQLdb.connect => begins the connection
	cursor = db_connect.cursor() => begind th curser
	cursor.excute => hold the query orders <br>
	query_rows = sql_order.fetchall() => holds all the data <br>
	cursor.close() => closes the cursor <br>
	db_connect.close() => closes the connection <br>
