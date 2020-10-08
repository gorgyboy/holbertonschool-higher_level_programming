#!/usr/bin/python3
''' I/O module
    Adds all arguments to a Python list, and then save them to a file.
'''

from sys import argv
from os import path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    if path.exists('add_item.json'):
        j_list = load_from_json_file('add_item.json')
    else:
        j_list = []
    for i in range(1, len(argv)):
        j_list.append(argv[i])
    save_to_json_file(j_list, 'add_item.json')
