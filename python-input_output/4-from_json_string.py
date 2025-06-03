#!/usr/bin/python3
"""The object representation of a JSON"""

import json


def from_json_string(my_string):
    """
    Return the object represented by a JSON string.
    """
    panda = json.loads(my_string)
    return panda
