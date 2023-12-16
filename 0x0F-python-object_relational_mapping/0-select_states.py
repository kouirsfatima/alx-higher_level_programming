 #!/usr/bin/python3
"""module for states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

  if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
