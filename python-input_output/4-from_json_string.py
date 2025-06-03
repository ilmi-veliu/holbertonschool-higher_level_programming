#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Return object represented by JSON string.
    """
    panda = json.dumps(my_str)
    return panda
