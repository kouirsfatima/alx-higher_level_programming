#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for char in str:
        if 'a' <= char <= 'z':
            str1 = str1 + chr(ord(char) - 32)
        else:
            str1 = str1 + char
    print("{}".format(str1))
