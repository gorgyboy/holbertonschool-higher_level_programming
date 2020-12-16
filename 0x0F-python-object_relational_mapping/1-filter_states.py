#!/usr/bin/python3
"""PYTHON OBJECT RELATIONAL MAPPING MODULE"""

import MySQLdb
from sys import argv


def filter_states():
    """
    Lists all states with a name starting with N (upper N) from the database.
    Receives username, password and datebase as arguments.
    """

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
