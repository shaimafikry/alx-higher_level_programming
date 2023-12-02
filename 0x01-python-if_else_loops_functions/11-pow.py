#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b == 0:
        return 1
    elif b < 0:
        b = b * -1
        while (b != 0):
             print (b)
             res = res * 1/a
             b = b - 1
    else:
        while (b != 0):
            print (b)
            res = res * a
            b = b - 1
    return res


print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(1000, -2))
print(pow(4, 5))
