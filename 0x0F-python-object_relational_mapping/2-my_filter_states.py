#!/usr/bin/python3
""" this module connect the database with python using argv
"""

import MySQLdb
from sys import argv

# script that takes in an argument and displays all values
# in the states table of hbtn_0e_0_usa where name matches the argument.
if __name__ == "__main__":
    u_name = argv[1]
    u_pass = argv[2]
    db_name = argv[3]
    port = 3306
    host = "localhost"
    db_access = MySQLdb.connect(host, u_name, u_pass, db_name, port)
    sql_order = db_access.cursor()
    sql_text = """SELECT * FROM states WHERE BINARY name =
                "{}" ORDER BY states.id ASC;""".format(argv[4])
    sql_order.execute(sql_text)
    query_rows = sql_order.fetchall()
    for row in query_rows:
        print(row)
    sql_order.close()
    db_access.close()
