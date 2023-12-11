#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        n_tup = (0 , 0)
        if len(tuple_a) == 0:
                x = 0
                y = 0
        elif len(tuple_a)  == 1:
                x = tuple_a[0]
                y = 0
        else:
            x = tuple_a[0]
            y = tuple_a[1]
        if len(tuple_b) == 0:
                z = 0
                m = 0
        elif len(tuple_b) == 1:
                z = tuple_a[0]
                m = 0
        else:
            z = tuple_b[0]
            m = tuple_b[1]
        lst =list(n_tup)
        lst[0] = x + z
        lst[1] = y + m
        n_tup = tuple(lst)
        return n_tup

tuple_a = (1, 89)
tuple_b = (88, 11, 2)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
