#!/usr/bin/python3

def main():
    # We can access command-line arguments directly without importing sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    calculator_code = open('calculator_1.py').read()
    calculator_locals = {}
    exec(calculator_code, {}, calculator_locals)

    if operator == '+':
        print(f"{a} + {b} = {calculator_locals['add'](a, b)}")
        exit(0)
    elif operator == '-':
        print(f"{a} - {b} = {calculator_locals['sub'](a, b)}")
        exit(0)
    elif operator == '*':
        print(f"{a} * {b} = {calculator_locals['mul'](a, b)}")
        exit(0)
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
        else:
            print(f"{a} / {b} = {calculator_locals['div'](a, b)}")
            exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

if __name__ == "__main__":
    import sys  # Import sys only when script is executed
    main()
