#!/usr/bin/python3
"""
   This scrpt takes args and the diplays the value of each state
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
    command = """SELECT *
                 FROM states
                 WHERE BINARY states.name = '{}'
                 ORDER BY states.id ASC"""
    command = command.format(argv[4])
    numrows = c.execute(command)
    states = c.fetchall()
    for idstate in states:
        print(idstate)


if __name__ == "__main__":
    main()
