#!/usr/bin/python3
""" Q0 """


import MySQLdb

if __name__ == '__main__':

    try:
        with MySQLdb.connect(
            host='localhost',
            port='',
            user='',
            passwd='',
            db=''
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * From states;')
        ...
    except Exception as e:
        print(e)
