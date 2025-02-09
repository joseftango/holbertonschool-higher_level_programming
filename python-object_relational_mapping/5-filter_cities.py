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
    cursor.execute('SELECT name FROM cities\
                    WHERE cities.state_id =\
                    (SELECT id FROM states WHERE name = "{}")\
                    ORDER BY cities.id ASC;'.format(state_name))

    rows = cursor.fetchall()
    print(', '.join(row[0] for row in rows))

    cursor.close()
    connection.close()
