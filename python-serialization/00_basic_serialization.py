#!/usr/bin/env python3
"""Basic serialization module using JSON format."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it to a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, "r") as file:
        return json.load(file)
