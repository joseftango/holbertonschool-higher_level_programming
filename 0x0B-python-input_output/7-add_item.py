#!/usr/bin/python3
import json
"""import json library"""


from sys import argv
"""import sys library"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""import 5-save_to_json_file module"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import 6-load_from_json_file module"""


try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

my_list = load_from_json_file("add_item.json")

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, "add_item.json")
