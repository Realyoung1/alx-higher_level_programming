#!/usr/bin/python3
"""
    Listings cities relatuonships
    states one databases
    this scripts takes two args
    this script conncected with MySQL
    I sorted the result in an ascending order
    The result was displayed based on the given examples
    I make sure my code was not executed when imported
"""
import sys
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
