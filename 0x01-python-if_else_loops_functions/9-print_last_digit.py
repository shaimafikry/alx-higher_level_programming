#!/usr/bin/python3
def print_last_digit(number):

    if number >= 0:
        m = number % 10
    else:
        m = number % -10
        m = m * -1
    print(m, end="")
    return m
