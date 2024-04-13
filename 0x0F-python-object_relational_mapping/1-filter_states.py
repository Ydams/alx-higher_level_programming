#!/usr/bin/python3
import MySQLdb
import sys

def get_states_starting_with_n(username, password, hbtn_0e_0_usa):
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

    # SQL query to get states starting with 'N'
    sql_query = """
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """

    try:
        # Execute the SQL query
        cursor.execute(sql_query)

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
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    get_states_starting_with_n(username, password, database_name)
