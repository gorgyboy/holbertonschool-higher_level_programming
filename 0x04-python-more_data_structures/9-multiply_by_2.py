#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    key_list = sorted(a_dictionary.keys())
    new_dict = {key: a_dictionary[key] * 2 for key in key_list}
    return new_dict
