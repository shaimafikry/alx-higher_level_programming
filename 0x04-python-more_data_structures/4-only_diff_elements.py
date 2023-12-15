#!/usr/bin/python3
# Write a function that returns a set of all elements present in only one set.

# Prototype: def only_diff_elements(set_1, set_2):
# You are not allowed to import any module
def only_diff_elements(set_1, set_2):
    set_o = set_1.difference(set_2)
    set_p = set_2.difference(set_1)
    set_w = list(set_p) + list(set_o)
    return set(set_w)
