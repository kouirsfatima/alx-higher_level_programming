#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    length = len(sentence)
    i = sentence[0]
    return (length, i)
