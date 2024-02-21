SQL
Structured query language (SQL) is a programming language for storing and processing information in a relational database. A relational database stores information in tabular form, with rows and columns representing different data attributes and the various relationships between the data values.

HOW to comment in SQL:
-- comment
"there is a space between -- and  comment"

NOTES:
* names of tables and columns and rows are written without ("")
* there is a "," to sepreate more than 1 column
* data type of every columns is written directly next to it without any additional data
	ex :  id INT (column name id of type INT) -->> CHECK (4-first_table.sql)
* we can use if conditoin in sql -->> CHECK (1-create_database_if_missing.sql, 2-remove_database.sql, 9-full_creation.sql)
* to show decription of how u created a table you can use -->> CHECK (5-full_table.sql)
* to get into a specific database you may use (USE database_name)
* to show fields ( columns) from a table use :
	1- SHOW FULL COLUMNS FROM table_name
	2- SHOW COLUMNS FROM table_name
	3- SHOW FIELDS FROM table_name
* to show rows you use (select)-->> CHECK (6-list_values.sql)
* to add a new row -->> CHECK (7-insert_value.sql, 9-full_creation.sql)
*  to know the count of rows -->> CHECK (8-count_89.sql)
* (ASC, DESC) used to show results in order-->> CHECK (10-top_score.sql)
* to get the average value of a column in a table and give a name to result -->> CHECK (14-average.sql)
* you may need to check if the data is null before showing it -->> CHECK (16-no_link.sql)
* The GROUP BY clause in SQL is used to group rows that have the same values in specified columns into summary rows,
   like "total quantity" or "average salary."
   It's often used with aggregate functions (like COUNT, MAX, MIN, SUM, AVG) to perform calculations on each group of
   rows. -->> CHECK (15-groups.sql)
