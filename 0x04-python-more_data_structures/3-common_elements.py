#!/usr/bin/python3
# Write a function that returns a set of common elements in two sets.
# Prototype: def common_elements(set_1, set_2):
# You are not allowed to import any module
def common_elements(set_1, set_2):
    nlist = []
    nset_1 = list(set_1)
    nset_2 = list(set_2)
    for i in nset_1:
        if i in nset_2:
            nlist.append(i)
    return set(nlist)
