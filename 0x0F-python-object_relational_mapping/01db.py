#!/usr/bin/python3
""" Q0 """


import mysql.connector
# import MySQLdb
try:

    with mysql.connector.connect(
        host='localhost',
        user=input('user: '),
        password=input('pass: ')
    ) as conn:
        print(conn)
        with conn.cursor() as cursor:
            cursor.execute('CREATE DATABASE Booking')

except Exception as e:
    print(e)