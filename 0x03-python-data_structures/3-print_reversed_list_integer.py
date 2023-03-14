#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """print all integers of a list in reversed order."""
    if isintance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
