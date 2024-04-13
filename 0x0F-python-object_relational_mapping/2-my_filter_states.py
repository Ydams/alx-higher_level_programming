#!/usr/bin/python3
import MySQLdb
import sys

def search_state_by_name(username, password, hbtn_0e_0_usa, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL query to search for state by name
    sql_query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
    """

    try:
        # Execute the SQL query with user input
        cursor.execute(sql_query, (state_name,))

        # Fetch all the rows
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <hbtn_0e_0_usa> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    search_state_by_name(username, password, database_name, state_name)
