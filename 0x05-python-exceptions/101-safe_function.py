#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        A = fct(*args)
        return A
    except Exception as todin:
        print("Exception: {}".format(todin), file=sys.stderr)
        return None
