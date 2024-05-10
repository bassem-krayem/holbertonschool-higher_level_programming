#!/usr/bin/python3
import sys


def add_all():
    total = 0
    for x in range(1, len(sys.argv)):
        total += int(sys.argv[x])
    print(total)


if __name__ == "__main__":
    add_all()
