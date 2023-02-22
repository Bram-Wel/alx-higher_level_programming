#!/usr/bin/python3
"""List all states from database {hbtn_0e_0_usa}."""

import MySQLdb

from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
        cursor = db.cursor()
        cursor.execute("""SELECT cities.id, cities.name, states.name
                        FROM cities INNER JOIN states ON
                        cities.state_id = states.id ORDER BY cities.id ASC""")
    except MySQLdb.Error as e:
        print(e)
    else:
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
        cursor.close()
        db.close()
