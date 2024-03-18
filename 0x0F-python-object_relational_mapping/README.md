<h1> Python - Object-relational mapping <h1>

	db_connect = MySQLdb.connect => begins the connection <br>
	cursor = db_connect.cursor() => begind th curser <br>
	cursor.excute => hold the query orders <br>
	query_rows = sql_order.fetchall() => holds all the data <br>
	cursor.close() => closes the cursor <br>
	db_connect.close() => closes the connection <br>
