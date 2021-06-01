#!/usr/bin/python3
"""This module writes """


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, 'w') as fil:
        fil.write(text)
    return len(text)
