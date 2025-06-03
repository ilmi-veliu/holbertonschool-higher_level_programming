#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Return object (Python data structure) represented by JSON string.
    """
    return json.loads(my_str)
