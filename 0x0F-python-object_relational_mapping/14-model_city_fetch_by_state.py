#!/usr/bin/python3
"""
    Gettingg all these states of databased
    states one databases
    this scripts takes two args
    this script conncected with MySQL
    I sorted the result in an ascending order
    The result was displayed based on the given examples
    I make sure my code was not executed when imported
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    main()
