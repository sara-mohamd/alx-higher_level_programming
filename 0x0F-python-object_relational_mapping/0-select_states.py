#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb

if __name__ == '__main__':

    try:
        """no argument validation needed"""
        with MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[0],
            passwd=argv[1],
            db=argv[2]
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * From states ORDERED BY  id ASC;')
        ...
    except Exception as e:
        print(e)
