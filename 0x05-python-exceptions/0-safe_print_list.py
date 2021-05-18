#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    Vp = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            Vp += 1
    except IndexError:
        None

    print()
    return Vp
