SQL - More queries
* How to create a new MySQL user?-->> CHECK (1-create_user.sql)
	- you may create a user by (mysql> CREATE USER "username@host" IDENTIFIED BY "password)
	* how about authentication plugin ?
		- it's added by defult when you use this way ^ (default = caching_sha2_password )
		- if you wanna add an "authentication" you add (IDENTIFIED WITH (ur_authentication) BY "password")
		NOTE:
		what is authentications plugin and what it used for?
		The authentication plugins in MySQL are components that implement authentication mechanisms. They are part of MySQL's pluggable authentication system, which allows for a flexible and extensible way to manage user authentication. These plugins can be used to implement various authentication methods, such as password-based authentication, token-based authentication, or even custom authentication schemes.
* How to show grants for a user ?
	- SHOW GRANTS FOR 'username'@'host';-->>check (0-privileges.sql)
* How to delete a user?
	- DROP USER 'username'@'localhost';

* How to manage privileges for a user to a database or table
	- if you want to give privillage to user , you have to own it first as a user
	- how ? like this :-->>check (2-create_read_user.sql)
		GRANT (privilage) # add more sepreated by comma (like: CREAT, INSERTM DROP..ETC), use (ALL)to give all
		ON database.table # data you give priviliage on , upu can replace it with *.* to give priv on all databases
		TO username 		# the user name you want to give privilage to
		WITH GRANT OPTION	#this line to make the user able to give privilages too
	- how to take priviliage back ?
		-sure, do this:
			REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';

* How to use NOT NULL and UNIQUE constraints?
	- it can be added right beside the type of the columns -->> CHECK ( 3-force_name.sql, 5-unique_id.sql)
	- there are a bunch of constrains on mysql columns like:
		-- NOT NULL 	# cant hold a null value
		-- UNIQUE		# cant hold the same value twice
		-- PRIMARY KEY  # uniquely identifies each record in a database table
		-- FOREIGN KEY  # A FOREIGN KEY in one table points to a PRIMARY KEY in another table
		-- ENUM 		#string object with a value chosen from a list of permitted values. They are enumerated explicitly in the 
						column specification at table creation time. we can put values like ('v1', 'v2', 'v3', etc)
		-- SET 			#string object with a value chosen from a list of permitted values. They are enumerated explicitly in the 
							column specification at table creation time.
		-- CHECK  		#for database to check valid data

		* NOTES:
			ENUM and SET propably the same in concept but enum allows only one value to be stored in  row and set allows one or more

	
* What’s a PRIMARY KEY?
	-The PRIMARY KEY constraint uniquely identifies each record in a database table. It is a special case of unique keys. Primary keys cannot be NULL, unique keys can be. There can be more UNIQUE columns, but only one primary key in a table. Primary keys are important when designing the database tables. Primary keys are unique ids. We use them to refer to table rows. Primary keys become foreign keys in other tables, when creating relations among tables.

* What’s a FOREIGN KEY
	-A FOREIGN KEY in one table points to a PRIMARY KEY in another table. It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.
	what would foreign key enforcement mean when use? 
	after we create a column in table_2 with the same name in table_1 that are related 
	We could not insert a row into table_2.name not exists in table_1.name.

* How to retrieve datas from multiple tables in one request?
	-by using JOIN, types:
		- INNER JOIN (JOIN): takes all  equals on both tables
		- LEFT JOIN (LEFT OUTER JOIN): takes all equals on left table even if there is no data in right table that meets it 
			(shows NULL instead)
		- RIGHT JOIN (RIGH OUTER JOIN): takes all equals on right table even if there is no data in left table that meets it 
			(shows NULL instead)

		- the left table : is the table before the join
		- the right table is the table after the join
		* Key Points:
			The left table is the one whose rows are returned in their entirety, regardless of whether there are matching rows in the right table.
			The right table's rows are only returned if there is a match in the left table based on the join condition.
			The choice between using a LEFT JOIN or a RIGHT JOIN depends on which table's rows you want to ensure are returned in full.


* What are subqueries?
	-it's like  command inside a command
	Subqueries, also known as inner queries or nested queries, are a powerful tool in SQL that allows you to perform operations in multiple steps within a single query. They can be used in various parts of a query, including the SELECT, FROM, WHERE, JOIN, and HAVING clauses. The subquery, or inner query, executes first, and its results are then used by the outer query. This functionality enables complex data manipulation and analysis within a single SQL statement.

* What are JOIN and UNION?
	-join acts as two tables puts together sie to side based on shared column.
	- there is must be one shared column at least to do the join , ot a columns with the same data type
	  you can do more that one join and the result becomes the new data for the other join statment

	  UNION:
	  collect data from tow select in one vertical result.

* Different functions:
 - IF(EXP, true, false)
 - NULLIF(exps, exps) returns null if two exps are equal or first exp if not
 - IFNULL(exp, exp)  It takes two arguments: the first is the expression to check for null, and the second is the value to return if 
 	the first expression is null.
 -

* WHAT is the order of command excuted in sql ?

	1 - FROM/JOIN: The FROM and/or JOIN clauses are executed first to determine the data of interest. This step merges the specified 
		tables and views into a single working set of data.
	2 - WHERE: The WHERE clause is executed to filter out records that do not meet the specified conditions.
	3 - GROUP BY: If a GROUP BY clause is present, it groups the filtered records based on the specified columns.
	4 - HAVING: The HAVING clause is executed to remove groups that do not meet the specified conditions.
	5 - SELECT: The SELECT clause is executed to derive all desired columns and expressions. This step operates on the result of the 
		previous operations, including any filtering, grouping, or joining that has occurred.
	6 - ORDER BY: The ORDER BY clause sorts the results based on the specified columns in either ascending or descending order.
	7 - LIMIT/OFFSET: Finally, the LIMIT and/or OFFSET clauses are executed to keep or skip a specified number of rows.
