#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
City = declarative_base()

# Define State class
class state(City):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Connecting to the MySQL server running on localhost at port 3306
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database_name')
    Base.metadata.create_all(engine)
