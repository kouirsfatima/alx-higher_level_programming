#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range (len(my_list)):
        if idx == 1 or idx >= len(my_list):
            return None
    print("Element at index {:d} is {}".format(i, my_list[i]))
