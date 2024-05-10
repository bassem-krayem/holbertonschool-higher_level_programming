# python-if_else_loops_functions:

## Description:

The Python - if/else, loops, functions project is tailored for novice learners, offering a structured introduction to essential Python concepts. Led by Guillaume, this project provides hands-on exercises focusing on if/else statements, loops, and functions, all crucial building blocks in Python programming.

## Learning Objectives:

At the end of this project, you are expected to be able to explain to anyone, without the help of Google.

## General:

- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## Requirements:

### Python Scripts:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.\*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.\*)
- All your files must be executable
- The length of your files will be tested using wc.

## Mandatory tasks:

### 0. Positive anything is better than negative nothing

#### Description:

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

#### Instructions:

- You don't need to understand what `import`, `random.randint` do. Please do not touch this code.
- The variable `number` will store a different value every time you run this program.
- The output of the program should be:
- The number, followed by:
- if the number is greater than 0: is positive
- if the number is 0: is zero
- if the number is less than 0: is negative
- followed by a new line

##### Example:

$ ./0-positive_or_negative.py \
-4 is negative\
$ ./0-positive_or_negative.py \
0 is zero\
$ ./0-positive_or_negative.py \
-3 is negative

### 1. The last digit

#### Description:

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

#### Instructions:

- You don't need to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
- The string "Last digit of", followed by
- the number, followed by
- the string "is", followed by the last digit of `number`, followed by:
- if the last digit is greater than 5: the string "and is greater than 5"
- if the last digit is 0: the string "and is 0"
- if the last digit is less than 6 and not 0: the string "and is less than 6 and not 0"
- followed by a new line

##### Example:

$ ./1-last_digit.py\
Last digit of 4205 is 5 and is less than 6 and not 0\
$ ./1-last_digit.py\
Last digit of -626 is -6 and is less than 6 and not 0

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

#### Description:

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

#### Instructions:

- Use only one `print` function with string format.
- Use only one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

##### Example:

$ ./2-print_alphabet.py\
abcdefghijklmnopqrstuvwxyz

### 3. When I was having that alphabet soup, I never thought that it would pay off

#### Description: Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line, excluding the letters 'q' and 'e'.

#### Instructions:

- Print all the letters except 'q' and 'e'.
- You can only use one `print` function with string format.
- You can only use one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

##### Example:

$ ./3-print_alphabt.py\
abcdfghijklmnoprstuvwxyz

### 4. Hexadecimal printing

#### Description:

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

#### Instructions:

- Use only one `print` function with string format.
- Use only one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

##### Example:

$ ./4-print_hexa.py\
0 = 0x0\
1 = 0x1\
...\
96 = 0x60\
97 = 0x61\
98 = 0x62

### 5. 00...99

#### Description: Write a program that prints numbers from 0 to 99.

#### Instructions:

- Numbers must be separated by ", " followed by a space.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- You can only use no more than 2 `print` functions with string format.
- You can only use one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

##### Example:

$ ./5-print_comb2.py\
00, 01, 02, ..., 99

### 6. Brains and Materials

#### Description:

Write a program that prints all possible different combinations of two digits.

#### Instructions:

- Numbers must be separated by ", " followed by a space.
- The two digits must be different.
- 01 and 10 are considered the same combination of the two digits 0 and 1.
- Print only the smallest combination of two digits.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- You can only use no more than 3 print functions with string format.
- You can only use no more than 2 loops in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

##### Example:

$ ./6-print_comb3.py\
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, \25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89

### 7. islower

#### Description: Write a function that checks for a lowercase character.

#### Instructions:

- Prototype: `def islower(c):`
- Returns True if `c` is lowercase.
- Returns False otherwise.
- You are not allowed to import any module.
- You are not allowed to use `str.upper()` and `str.isupper()`.
- Tips: `ord()`

##### Example:

$ cat 7-main.py\
#!/usr/bin/env python3\
islower = **import**('7-islower').islower\

print("a is {}".format("lower" if islower("a") else "upper"))\
print("H is {}".format("lower" if islower("H") else "upper"))\
print("A is {}".format("lower" if islower("A") else "upper"))\
print("3 is {}".format("lower" if islower("3") else "upper"))\
print("g is {}".format("lower" if islower("g") else "upper"))\

$ ./7-main.py\
a is lower\
H is upper\
A is upper\
3 is upper\
g is lower

### 8. To uppercase

#### Description:

Write a function that prints a string in uppercase followed by a new line.

#### Instructions:

- Prototype: `def uppercase(str):`
- You can only use no more than 2 `print` functions with string format.
- You can only use one loop in your code.
- You are not allowed to import any module.
- You are not allowed to use `str.upper()` and `str.isupper()`.
- Tips: `ord()`

##### Example:

$ cat 8-main.py\
#!/usr/bin/env python3\
uppercase = **import**('8-uppercase').uppercase\

uppercase("best")\
uppercase("Best School 98 Battery street")\

$ ./8-main.py\
BEST\
BEST SCHOOL 98 BATTERY STREET

### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important

#### Description: Write a function that prints the last digit of a number.

#### Instructions:

- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit.
- You are not allowed to import any module.
- You don't need to understand `__import__`.

##### Example:

$ cat 9-main.py\
#!/usr/bin/env python3\
print_last_digit = **import**('9-print_last_digit').print_last_digit\

print_last_digit(98)\
print_last_digit(0)\
r = print_last_digit(-1024)\
print(r)\

$ ./9-main.py\
8044

### 10. a + b

#### Description:

Write a function that adds two integers and returns the result.

#### Instructions:

- Prototype: `def add(a, b):`
- Returns the value of `a + b`.
- You are not allowed to import any module.
- You don't need to understand `__import__`.

##### Example:

$ cat 10-main.py\
#!/usr/bin/env python3\
add = **import**('10-add').add\

print(add(1, 2))\
print(add(98, 0))\
print(add(100, -2))\

$ ./10-main.py\
3\
98\
98

### 11. a ^ b\

#### Description:

Write a function that computes `a` to the power of `b` and returns the value.

#### Instructions:

- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`.
- You are not allowed to import any module.
- You don't need to understand `__import__`.

##### Example:

$ cat 11-main.py\
#!/usr/bin/env python3\
pow = **import**('11-pow').pow\

print(pow(2, 2))\
print(pow(98, 2))\
print(pow(98, 0))\
print(pow(100, -2))\
print(pow(-4, 5))\

$ ./11-main.py\
4\
9604\
1\
0.0001\
-1024

### 12. Fizz Buzz

#### Description:

Write a function that prints the numbers from 1 to 100 separated by a space.

#### Instructions:

- For multiples of three, print "Fizz" instead of the number.
- For multiples of five, print "Buzz" instead of the number.
- For numbers which are multiples of both three and five, print "FizzBuzz".
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space.
- You are not allowed to import any module.
- You don't need to understand `__import__`.

##### Example:

$ cat 12-main.py\
#!/usr/bin/env python3\
fizzbuzz = **import**('12-fizzbuzz').fizzbuzz\

fizzbuzz()\
print("")\

$ ./12-main.py | cat -e\
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz \Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 \Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 \Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 \Fizz 94 Buzz Fizz 97 98 Fizz Buzz \
