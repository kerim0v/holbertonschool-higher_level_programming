#!/usr/bin/python3
"""Lists all cities of a state, safe from SQL injection."""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = ("SELECT cities.id, cities.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
