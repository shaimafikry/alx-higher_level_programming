#!/usr/bin/python3
# Write a function that adds all unique integers in a list (only once for each integer).
# Prototype: def uniq_add(my_list=[]):
# You are not allowed to import any module
def uniq_add(my_list=[]):
    m = 0
    new_list = list(set(my_list.copy()))
    for i in new_list:
        m = m + i
    return m
