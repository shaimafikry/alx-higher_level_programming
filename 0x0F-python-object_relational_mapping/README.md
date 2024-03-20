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

* SQL injection:
	- happesn when you use concating to add user input to the sql command
	- this  allow hackers to add (Sql statements instead of (normal user input) and make it run to ur database)
	*To Avoid this => use string formts (%s) to hanlde user input and adding it to the sql command
	[more details](https://www.w3schools.com/sql/sql_injection.asp)
* SQL search patterns
* SQL search is not case sensitive :

	if i want to search for names starts with letter (n)
	i can use :
		* LIKE 'N%' => to  use wild cards
		* RLIKE '^N' => to use regex
		* REGEXP_LIKE(name, 'N%' COLLATE utf8mb4_0900_as_cs);
		* REGEXP_LIKE(name, '^N');
		- in case you want it case sensitive , to show only upper case N:
				* REGEXP_LIKE(name, '^N' COLLATE utf8mb4_0900_as_cs)
		[more detials](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.3/en/pattern-matching.html)
		
		
	
