#!/usr/bin/python3
"""
    This is the cripted that list all states objects from a databased
    this scripts takes two args
    this script conncected with MySQL
    I sorted the result in an ascending order
    The result was displayed based on the given examples
    I make sure my code was not executed when imported
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    result = engine.execute('SELECT * FROM states ORDER BY states.id ASC')
    for row in result:
        print("{}: {}".format(row[0], row[1]))


if __name__ == "__main__":
    main()
