#!/usr/bin/python3
'''1-filter_states module'''
from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=database)

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM states WHERE name LIKE "N%"\
                   OR name LIKE "n%" ORDER BY id ASC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
