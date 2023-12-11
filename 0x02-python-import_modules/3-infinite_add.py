#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    num = 0
    for i in range(1, len(argv)):
        num = num + int(argv[i])
    print("{:d}".format(num))
