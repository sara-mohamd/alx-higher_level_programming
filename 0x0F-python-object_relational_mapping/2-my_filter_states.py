#!/usr/bin/python3
""" write script that takes name of db as an arg """


import MySQLdb
from sys import argv


if __name__ == '__main__':

    try:
        with MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            name=argv[4]
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * From states ORDER BY id ASC;')
                for data in cur.fetchall():
                    print(data)

    except Exception as e:
        print("MySQL Error:", e)
