#!/usr/bin/python3
import sys
from calculator import add, sub, mul, div


def main():

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit("1")

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == '+':
        print(f"{a} + {b} = {add(a, b)}")
        exit("0")
    elif operator == '-':
        print(f"{a} - {b} = {sub(a, b)}")
        exit("0")
    elif operator == '*':
        print(f"{a} * {b} = {mul(a, b)}")
        exit("0")
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
        else:
            print(f"{a} / {b} = {div(a, b)}")
            exit("0")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit("1")


if __name__ == "__main__":
    main()
