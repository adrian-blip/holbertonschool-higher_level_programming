#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
