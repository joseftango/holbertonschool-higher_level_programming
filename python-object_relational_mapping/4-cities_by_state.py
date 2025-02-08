#!/usr/bin/python3
'''3-my_safe_filter_states module'''
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states WHERE cities.state_id = states.id\
                    ORDER BY cities.id ASC;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
