#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    tmp_list = my_list
    tmp_list.reverse()
    for i in tmp_list:
        print("{:d}".format(i))
