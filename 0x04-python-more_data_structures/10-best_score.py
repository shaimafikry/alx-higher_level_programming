#!/usr/bin/python3
# function that returns a key with the biggest integer value.(a_dictionary):
# You can assume all values only integers
# If no score found, return None
# You can assume all students have a different score
# You are not allowed to import any module
def best_score(a_dictionary):
    if a_dictionary:
        r = 0
        for k, m in a_dictionary.items():
            if m > r:
                r = m
        for k, m in a_dictionary.items():
            if r == m:
                return k
    else:
        return None
