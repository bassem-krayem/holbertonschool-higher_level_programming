#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list = my_list[::-1]
    for x in range(len(list)):
        print("{:d}\n".format(list[x]), end="")
