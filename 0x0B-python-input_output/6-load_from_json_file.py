#!/usr/bin/python3
"""Takes a json file"""


import json


def load_from_json_file(filename):
    """insert module documentation here as well"""
    with open(filename, 'r') as fil:
        return json.loads(fil.read())
