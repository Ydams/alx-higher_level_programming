#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, hbtn_0e_6_usa):
    # Create engine to connect to MySQL server
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn_0e_6_usa}")
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    try:
        # Create a new State object
        new_state = State(name="Louisiana")
        
        # Add the new state to the session
        session.add(new_state)
        
        # Commit the session to save the new state to the database
        session.commit()
        
        # Print the new state's id
        print(new_state.id)
            
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
    
    add_state(username, password, database_name)
