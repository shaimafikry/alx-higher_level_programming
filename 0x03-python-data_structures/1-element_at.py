#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    else:
        if idx in my_list:
            return my_list[idx]
        else:
            return None
