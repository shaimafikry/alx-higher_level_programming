#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    m = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                m = m + 1
        print()
        return m
    except:
        print("list index out of range")
