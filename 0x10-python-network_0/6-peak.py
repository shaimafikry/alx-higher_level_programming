#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        le = len(list_of_integers)
        first = list_of_integers[0]
        last = list_of_integers[-1]
        i = 0
        first_range = 0
        last_range = -1
        while (le > 0):
            if first > i:
                i = first
            if last > i:
                i = last
            le = le - 2
            first_range += 1
            last_range -= 1
            first = list_of_integers[first_range]
            last = list_of_integers[last_range]
        return i
    else:
        return None
