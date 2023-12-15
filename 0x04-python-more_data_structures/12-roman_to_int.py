#!/usr/bin/python3
# You are not allowed to google anything
# Whiteboard first
# Create a function def roman_to_int(roman_string): that
# converts a Roman numeral to an integer.
# You can assume the number will be between 1 to 3999.
# def roman_to_int(roman_string) must return an integer
# If the roman_string is not a string or None, return 0
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    r_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    list_num = list()
    for i in roman_string:
        for key in r_num:
            if i == key:
                list_num.append(r_num[key])
    list_num = list(list_num)
    m = list_num[0]
    n = -1
    for i in list_num:
        if m >= i:
            num = num + i
        else:
            num = i - num
        m = list_num[n + 1]
    return num
