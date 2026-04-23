#!/usr/bin/python3

def uppercase(str):
    for i in range(str):
        print("{}".format(str[i] if ord('A') <= ord(i) <= ord('Z') else str[i - 32]))
