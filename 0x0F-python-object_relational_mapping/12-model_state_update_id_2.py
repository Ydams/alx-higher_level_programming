#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, hbtn_0e_6_usa):
    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn_0e_6_usa}")

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Query to get the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            # Change the name to "New Mexico"
            state_to_update.name = "New Mexico"

            # Commit the session to save the changes to the database
            session.commit()

            print("State name updated successfully.")
        else:
            print("State with id = 2 not found.")

    except Exception as e:
        # Rollback the session in case of an error
        session.rollback()
        print("Error:", e)

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    change_state_name(username, password, database_name)
