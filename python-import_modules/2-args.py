#!/usr/bin/python3
import sys

def arguments():
    args = sys.argv
    num_args = len(args) - 1
    if num_args == 0:
        print("0 arguments")
    else:
        print(f"{num_args} argument")

    for x in range(1, len(args)):
        print(f"{x}: {args[x]}")

if __name__ == "__main__":
    arguments()
