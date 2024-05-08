#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if chr(x) in ['e', 'q']:
        continue
    print("{}".format(chr(x)), end="")
