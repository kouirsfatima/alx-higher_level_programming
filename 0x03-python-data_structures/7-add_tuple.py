#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tp2 = tuple_b[0] if len(tuple_b) > 0 else 0

    a = tuple_a[1] if len(tuple_a) > 1 else 0
    b = tuple_b[1] if len(tuple_b) > 1 else 0

    sum1 = tp1 + tp2
    sum2 = a + b

    new_tuple = (sum1, sum2)

    return new_tuple
