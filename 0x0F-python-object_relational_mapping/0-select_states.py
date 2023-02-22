#!/usr/bin/python3
"""List all states from database {hbtn_0e_0_usa}."""

import MySQLdb

from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM hbtn_0e_0_usa.states""")
    except MySQLdb.Error as e:
        # print(e)
        pass
    else:
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
        cursor.close()
        db.close()
