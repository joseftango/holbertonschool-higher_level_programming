#!/usr/bin/python3
"""function that creates an object in json file """

import json


def load_from_json_file(filename):
    """import jason module"""
    with open(filename, "r", encoding="utf-8") as f:
        jo = json.loads(f.read())
    return jo
