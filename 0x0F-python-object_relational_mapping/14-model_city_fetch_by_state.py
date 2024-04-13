#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, hbtn_0e_14_usa):
    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn_0e_14_usa}")

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    try:
        # Query to get all City objects
        cities = session.query(City).order_by(City.id).all()

        # Display results
        for city in cities:
            state_name = session.query(State).filter_by(id=city.state_id).first().name
            print(f"{state_name}: ({city.id}) {city.name}")

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

    fetch_cities_by_state(username, password, database_name)
