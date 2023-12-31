#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        x > 0
    except x == 0:
        print()
    for i, val in enumerate(my_list):
        print(val, end="")
        if (i + 1) == x:
            break
    print()
    return i + 1
