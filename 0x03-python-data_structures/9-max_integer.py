#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    big = 0
    for i in my_list:
        if i > big:
            big = i
    return big
