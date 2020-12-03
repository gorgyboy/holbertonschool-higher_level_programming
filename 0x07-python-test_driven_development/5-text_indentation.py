#!/usr/bin/python3
"""
5-text_identation module
"""


def text_indentation(text):
    """
    Prints <text> with 2 new lines after each of these
    characters: '.', '?' and ':'
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    idx = 0
    while idx < len(text):
        if text[idx] in ('.', '?', ':'):
            print(text[idx] + '\n')
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
        else:
            print(text[idx], end='')
            idx += 1
