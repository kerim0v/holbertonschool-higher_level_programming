#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        print("{}".format(str[i] if ord('A') <= ord(str[i]) <= ord('Z') else chr(ord(str[i]) - 32)), end='')
