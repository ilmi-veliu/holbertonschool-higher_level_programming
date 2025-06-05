#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Save dict to JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load dict from JSON file."""
    with open(filename, "r") as p:
        return json.load(p)
