#!/usr/bin/python3
"""
Lists all cities by state
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cursor =db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            LEFT JOIN states ON states.id = cities.state_id\
            ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for location in rows:
        print(location)
