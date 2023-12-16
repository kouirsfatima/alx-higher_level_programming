#!/usr/bin/python3
"""lists all cities with a name starting with N"""
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
    name_state= argv[4]
    curs.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id ASC"""(name_state))

    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)

    db.close()
