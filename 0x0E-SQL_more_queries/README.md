SQL - More queries
* How to create a new MySQL user
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
	- how ? like this :
		GRANT (privilage) # add more sepreated by comma (like: CREAT, INSERTM DROP..ETC), use (ALL PRIVILAGES)to give all
		ON database.table # data you give priviliage on , upu can replace it with *.* to give priv on all databases
		TO username 		# the user name you want to give privilage to
		WITH GRANT OPTION	#this line to make the user able to give privilages too
	- how to take priviliage back ?
		-sure, do this:
			REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';
What’s a PRIMARY KEY
What’s a FOREIGN KEY
How to use NOT NULL and UNIQUE constraints
How to retrieve datas from multiple tables in one request
What are subqueries
What are JOIN and UNION
