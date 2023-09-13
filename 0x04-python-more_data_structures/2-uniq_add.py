#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    _list = set(my_list)
    for i in _list:
        num += i
    return num
