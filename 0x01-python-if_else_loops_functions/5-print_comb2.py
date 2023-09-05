#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        ptr = "\n"
    else:
        ptr = ", "
    print("{:02d}".format(i), end=ptr)
