#!/usr/bin/python3
"""The JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    panda = json.dumps(my_obj)
    return panda
