#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    curs = db.cursor()
    state_name = argv[4]

    curs.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))

    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)

    db.close()
