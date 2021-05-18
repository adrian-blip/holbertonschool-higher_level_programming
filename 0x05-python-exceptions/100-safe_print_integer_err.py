#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as idon:
        print("Exception: {}".format(idon), file=sys.stderr)
        return False

     

