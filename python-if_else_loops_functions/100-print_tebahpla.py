#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, - 1):
    lettre = chr(x)
    if x % 2 != 0:
        lettre = chr(x - 32)

    print("{}".format(lettre), end="")
