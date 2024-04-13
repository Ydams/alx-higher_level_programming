#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, hbtn_0e_6_usa):
    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn_0e_6_usa}")

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Query to get all State objects with names containing 'a'
        states_with_a = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

        # Display results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

    except Exception as e:
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

    list_states_with_letter_a(username, password, database_name)
