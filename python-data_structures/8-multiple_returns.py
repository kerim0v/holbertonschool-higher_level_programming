#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_a = (0, None)
        return tuple_a
    tuple_b = (len(sentence), sentence[0])
    return tuple_b
