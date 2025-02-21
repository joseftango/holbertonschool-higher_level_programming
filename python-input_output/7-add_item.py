#!/usr/bin/python3
'''7-add_item module'''
from sys import argv
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = list()

if os.path.isfile('add_item.json'):
    my_list += load_from_json_file('add_item.json')
my_list += argv[1:]
save_to_json_file(my_list, 'add_item.json')
