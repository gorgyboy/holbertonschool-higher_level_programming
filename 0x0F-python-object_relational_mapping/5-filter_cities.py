#!/usr/bin/python3
"""PYTHON OBJECT RELATIONAL MAPPING MODULE"""

import MySQLdb
from sys import argv


def filter_cities():
    """
    Takes in the name of a state as an argument and lists all cities of that
    state, using the database.

    Takes  4 arguments: mysql username, mysql password, database name and
    state name (SQL injection free!).
    """

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id = ("
                "SELECT id FROM states "
                "WHERE name LIKE %s"
                ") ORDER BY id ASC", (argv[4], ))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        print(query_rows[i][0], end='')
        if i < len(query_rows) - 1:
            print(',', end=' ')
    print()
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_cities()
