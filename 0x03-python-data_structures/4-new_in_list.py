#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    tmp_list = my_list.copy()
    if not my_list or idx < 0 or idx >= len(tmp_list):
        return tmp_list
    else:
        tmp_list[idx] = element
        return tmp_list
