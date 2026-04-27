#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    if num == 1:
       print("1 argument:") 
    elif num == 0:
        print("0 arguments.") 
    else:
        print ("{} arguments:".format(num))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
