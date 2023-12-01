#!/usr/bin/python3
for i in range(9):
    for x in range(i+1, 10):
        if x != i:
            if i == 8 and x == 9:
                print("{}{}".format(i, x))
                break
            print("{}{}".format(i, x), end=', ')
