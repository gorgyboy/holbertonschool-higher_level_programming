#!/usr/bin/python3
"""PYTHON OBJECT RELATIONAL MAPPING MODULE"""

import MySQLdb
from sys import argv


def my_filter_states():
    """
    Takes in an argument and displays all values in the states table of the
    database where name matches the argument.

    Recieves 4 arguments: mysql username, mysql password, database name and
    state name searched.
    """

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    str1 = "SELECT * FROM states WHERE name LIKE BINARY '"
    str2 = "' ORDER BY id ASC"
    cur.execute("{}{}{}".format(str1, argv[4], str2))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    my_filter_states()
