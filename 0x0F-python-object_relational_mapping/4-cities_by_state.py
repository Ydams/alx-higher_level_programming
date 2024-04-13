#!/usr/bin/python3
import MySQLdb
import sys

def list_all_cities(username, password, hbtn_0e_4_usa):
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

    # SQL query to list all cities in ascending order by id
    sql_query = """
        SELECT * FROM cities
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

    list_all_cities(username, password, database_name)
