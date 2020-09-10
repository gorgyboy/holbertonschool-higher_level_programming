#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    new_list = my_list.copy()
    len_list = len(my_list)

    if my_list:
        if idx < 0 or idx >= len_list:
            return my_list
        else:
            my_list.clear()
            for i in range(len_list):
                if i != idx:
                    my_list.append(new_list[i])
            return my_list
    else:
        return my_list
