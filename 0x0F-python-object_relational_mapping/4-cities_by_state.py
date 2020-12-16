#!/usr/bin/python3
"""PYTHON OBJECT RELATIONAL MAPPING MODULE"""

import MySQLdb
from sys import argv


def cities_by_state():
    """
    List all cities from the database.
    Takes 3 arguments: mysql username, mysql password and database name.
    """

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id=states.id "
                "ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    cities_by_state()
