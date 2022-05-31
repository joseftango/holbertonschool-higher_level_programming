#!/usr/bin/python3
"""function that writes an Object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        new_obj = json.dumps(my_obj)
        f.write(new_obj)
