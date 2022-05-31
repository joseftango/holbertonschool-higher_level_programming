#!/usr/bin/python3
"""function that returns a JSON representation of an object string"""

import json


def to_json_string(my_obj):
    """json module"""

    return json.dumps(my_obj)
