#!/usr/bin/python3
'''3-my_safe_filter_states module'''
from sys import argv
import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    connection = MySQLdb.connect(host='localhost',
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=database)

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
