#!/usr/bin/python3
""" this module connect the database with python using argv
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    u_name = argv[1]
    u_pass = argv[2]
    db_name = argv[3]
    port = 3306
    host = "localhost"
    db_access = MySQLdb.connect(host, u_name, u_pass, db_name, port)
    sql_order = db_access.cursor()
    sql_order.execute(
        "SELECT name FROM cities WHERE state_id = (SELECT id from states WHERE name = %s) ORDER BY cities.id ASC;",
        (argv[4],),
    )
    n_list = []
    query_rows = sql_order.fetchall()
    for row in query_rows:
        n_list.append(row[0])
    print(", ".join(n_list))
    sql_order.close()
    db_access.close()
