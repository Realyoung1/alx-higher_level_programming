#!/usr/bin/python3
"""
    the scripts listed all states from the database hbtn_0e_0_usa
    this scripts takes two args
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
    numrows = c.execute("""SELECT * FROM states""")
    states = c.fetchall()
    for idstate in states:
        print(idstate)

if __name__ == "__main__":
    main()
