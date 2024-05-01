#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    if list_of_integers:
        m = 0
        for i in list_of_integers:
            if i > m:
                m = i
        return i
    else:
        return None
