#!/usr/bin/python3
"""function that returns a JSON representation of an object string"""

import json
"""json module"""


def to_json_string(my_obj):

    return json.dumps(my_obj)
