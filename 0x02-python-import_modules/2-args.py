#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count >= 2:
        print("{} arguments:".format(count))
    else:
        print("{} argument:".format(count))
    for i in range(1, len(argv)):
        print("{:d}: {}".format((i), argv[i]))
