#!/usr/bin/python3
"""
    Getting the cities one of state of a databased
    this scripts takes two args
    this script conncected with MySQL
    I sorted the result in an ascending order
    The result was displayed based on the given examples
    I make sure my code was not executed when imported
"""
import MySQLdb
from sys import argv


def main():
    """I only executed my codes is not imported"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    command = """SELECT cities.name
                 FROM cities, states
                 WHERE BINARY states.name = %s
                 AND cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    numrows = c.execute(command, (argv[4],))
    states = c.fetchall()
    print(", ".join(citistate[0] for citistate in states))


if __name__ == "__main__":
    main()
