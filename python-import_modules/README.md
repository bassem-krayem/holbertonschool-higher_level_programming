# Python - Import & Modules

## Description:

This project delves into the world of Python modules and imports, demonstrating how to leverage external code to enhance your programs. It covers importing functions and variables, creating modules, understanding the `dir()` function, and managing command-line arguments.

## Learning Objectives:

By the end of this project, you should be able to:

- Explain the significance of modules in Python.
- Import functions and variables from other files.
- Create and utilize your own Python modules.
- Employ the built-in `dir()` function to inspect module contents.
- Control code execution upon import.
- Effectively handle command-line arguments in Python scripts.

## Requirements:

- **Allowed editors:** vi, vim, emacs
- **Execution environment:** Ubuntu 22.04 LTS using python3 (version 3.10.\*)
- **Code style:** Adhere to pycodestyle (version 2.7.\*)
- **File formatting:**
  - All files must end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
- **Execution:** All files must be executable.
- **README.md:** A README.md file is mandatory at the project root.

## Tasks:

<details>
<summary>0. Import a simple function from a simple file</summary>

**Description:**
Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition 1 + 2 = 3.

**Instructions:**

- You have to use the `print` function with string format to display integers.
- Assign:
  - The value 1 to a variable called `a`
  - The value 2 to a variable called `b`
  - Use these variables as arguments when calling the `add` and `print` functions.
- Define `a` and `b` in separate lines: `a = 1` and `b = 2`
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- You can only use the word `add_0` once in your code.
- Do not use `*` for importing or `__import__`.
- Your code should not be executed when imported (use `__import__`, if necessary).

**Example:**

Use code with caution (opens in a new window)
Copy code
guillaume@ubuntu:~$ ./0-add.py
1 + 2 = 3

</details>

<details>
<summary>1. My first toolbox!</summary>

**Description:**
Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

**Instructions:**

- Do not use the `print` function (with string format to display integers) more than 4 times.
- Define:
  - The value 10 to a variable `a`
  - The value 5 to a variable `b`
  - Use these two variables only as arguments when calling functions (including `print`).
- Define `a` and `b` in separate lines: `a = 10` and `b = 5`
- Your program should call each of the imported functions.
- The word `calculator_1` should be used only once in your file.
- Do not use `*` for importing or `__import__`.
- Your code should not be executed when imported.

**Example:**

guillaume@ubuntu:~$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 \* 5 = 50
10 / 5 = 2

</details>

<details>
<summary>2. How to make a script dynamic!</summary>

**Description:**
Write a program that prints the number of and the list of its arguments.

**Instructions:**

- The output should be:
  - Number of argument(s) followed by "argument" (if the number is one) or "arguments" (otherwise), followed by
  - ":" (or "." if no arguments were passed) followed by
  - a new line, followed by (if at least one argument),
  - one line per argument:
    - the position of the argument (starting at 1) followed by ":", followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of `argv` can be retrieved by using: `len(argv)`

**Example:**

guillaume@ubuntu:~$ ./2-args.py
0 arguments.
guillaume@ubuntu:~$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School

</details>

<details>
<summary>3. Infinite addition</summary>

**Description:**
Write a program that prints the result of the addition of all arguments.

**Instructions:**

- The output should be the result of the addition of all arguments, followed by a new line.
- You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers).
- Your code should not be executed when imported.
- Your program should also handle big numbers.

**Example:**

guillaume@ubuntu:~$ ./3-infinite_add.py
0
guillaume@ubuntu:~$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~$ ./3-infinite_add.py 79 10 -40 -300 89
-162

</details>

<details>
<summary>4. Who are you?</summary>

**Description:**
Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

**Instructions:**

- This task must be done on the sandbox only.
- File `4-hidden_discovery.py` must be located in the folder `/tmp/`.
- You should print one name per line, in alpha order.
- You should print only names that do not start with `__`.
- Your code should not be executed when imported.

**Example:**

guillaume@ubuntu:/tmp$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school

</details>

<details>
<summary>5. Everything can be imported</summary>

**Description:**
Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

**Instructions:**

- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

**Example:**

guillaume@ubuntu:~$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""
guillaume@ubuntu:~$ ./5-variable_load.py
98

</details>

<details>
<summary>6. Build my own calculator! (Advanced)</summary>

**Description:**
Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.

**Instructions:**

- Usage: `./100-my_calculator.py a operator b`
  - If the number of arguments is not 3, your program has to:
    - Print `Usage: ./100-my_calculator.py <a> <operator> <b>` followed by a new line
    - Exit with the value 1
  - `operator` can be:
    - `+` for addition
    - `-` for subtraction
    - `*` for multiplication
    - `/` for division
  - If the operator is not one of the above:
    - Print `Unknown operator. Available operators: +, -, * and /` followed by a new line
    - Exit with the value 1
  - You can cast `a` and `b` into integers by using `int()` (you can assume that all arguments will be castable into integers)
  - The result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line

**Example:**

guillaume@ubuntu:~$ ./100-my_calculator.py\
Usage: ./100-my_calculator.py <a> <operator> <b>\
guillaume@ubuntu:~$ ./100-my_calculator.py 3 + 5\
3 + 5 = 8\
guillaume@ubuntu:~$ ./100-my_calculator.py 3 H 5\
Unknown operator. Available operators: +, -, \* and /

</details>

</details>
