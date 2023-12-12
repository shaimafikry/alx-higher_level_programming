#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    m = 0
    for m in range(len(new_list)):
        if new_list[m] == search:
            new_list[m] = replace
    return new_list
