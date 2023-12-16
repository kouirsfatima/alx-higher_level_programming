 #!/usr/bin/python3
"""module for states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    cou= MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    curs = cou.cursor()

    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    cou.close()
