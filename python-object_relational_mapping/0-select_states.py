#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute SQL query to get all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Display each row
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
