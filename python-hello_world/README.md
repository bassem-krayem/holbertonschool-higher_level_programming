# Python hello world:

## Description:

The Python - Hello, World project is designed to introduce beginners to Python programming by demonstrating fundamental concepts through a series of script tasks. The project aims to provide hands-on experience with Python syntax, basic operations, and best practices, while encouraging learners to explore different approaches to problem-solving.

### Key Objectives:

1. Introduction to Python: The project starts with simple tasks to familiarize learners with basic Python syntax and programming concepts.
2. Printing Output: Learners will practice using the `print` function to display text and variable values in the terminal.
3. String Manipulation: Tasks involve working with strings, including concatenation, slicing, and formatting.
4. Variable Operations: Learners will perform operations on variables, including integers and floats, to understand data manipulation in Python.
5. Coding Standards: The project emphasizes adhering to Python's official coding style guide (PEP8) and using tools like `pycodestyle` to ensure clean and readable code.

## Learning Objectives:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google.

## General:

- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle.

## Requirements:

### Python Scripts:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.\_)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.\_)
- All your files must be executable
- The length of your files will be tested using wc.

## Mandatory tasks:

### 0. Hello, print

#### Description:

Write a Python script that prints exactly "Programming is like building a multilingual puzzle", followed by a new line.

#### Instructions:

- Use the `print` function.

##### Example:

$ ./2-print.py
"Programming is like building a multilingual puzzle

### 1. Print integer

#### Description:

Complete this source code to print the integer stored in the variable `number`, followed by "Battery street", followed by a new line.

#### Instructions:

- You are not allowed to cast the variable `number` into a string.
- Your code must be 3 lines long.
- You have to use f-strings.

##### Example:

$ ./3-print_number.py
98 Battery street

### 2. Print float

#### Description:

Complete the source code to print the float stored in the variable `number` with a precision of 2 digits.

#### Instructions:

- You are not allowed to cast `number` to string.
- You have to use f-strings.

##### Example:

$ ./4-print_float.py
Float: 3.14

### 3. Print string

#### Description:

Complete this source code to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

#### Instructions:

- You are not allowed to use any loops or conditional statement.
- Your program should be maximum 5 lines long.

##### Example:

$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton

### 4. Play with strings

#### Description:

Complete this source code to print "Welcome to Holberton School!".

#### Instructions:

- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code.
- Your program should be exactly 5 lines long.

##### Example:

$ ./6-concat.py
Welcome to Holberton School!

### 5. Copy - Cut - Paste

#### Description:

Complete this source code to print various manipulations of the variable `word`.
####Instructions:

- You are not allowed to use any loops or conditional statements.
- Your program should be exactly 8 lines long.
- `word_first_3` should contain the first 3 letters of `word`.
- `word_last_2` should contain the last 2 letters of `word`.
- `middle_word` should contain `word` without the first and last letters.

##### Example:

$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto

### 6. Create a new sentence

#### Description:

Complete this source code to print "object-oriented programming with Python", followed by a new line.

#### Instructions:

- You are not allowed to use any loops or conditional statements.
- Your program should be exactly 5 lines long.
- You are not allowed to create new variables.
- You are not allowed to use string literals.

##### Example:

$ ./8-concat_edges.py
object-oriented programming with Python

### 7. Easter Egg

#### Description:

Write a Python script that prints "The Zen of Python", by Tim Peters, followed by a new line.

#### Instructions:

- Your script should be maximum 98 characters long.

##### Example:

$ ./9-easter*egg.py\
The Zen of Python, by Tim Peters\\
Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than \_right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!\
