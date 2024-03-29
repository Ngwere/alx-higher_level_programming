#!/usr/bin/python3
"""
Display all values in states that match name
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for state in rows:
        print(state)
