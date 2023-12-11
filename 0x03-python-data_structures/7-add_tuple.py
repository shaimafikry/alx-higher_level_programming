#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not len(tuple_a) and not len(tuple_b):
        t = (0, 0)
    if not len(tuple_a):
        t = tuple_b
    elif not len(tuple_b):
        t = tuple_a
    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        t = (tuple_a[0] + tuple_b[0], 0)
    elif len(tuple_a) < 2:
        t = (tuple_a[0] + tuple_b[0], tuple_b[1])
    elif len(tuple_b) < 2:
        t = (tuple_b[0] + tuple_a[0], tuple_a[1])
    else:
        t= (tuple_a[0] + tuple_b[0], tuple_b[1] + tuple_a[1])
    return t