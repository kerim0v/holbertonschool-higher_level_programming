#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    for i in range (0, len(argv)):
        sum = sum + argv[i]
    print(sum)
