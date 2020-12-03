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

    indentation = False
    for char in text:
        if char in ('.', '?', ':'):
            print(char + '\n')
            indentation = True
        else:
            if indentation is True:
                indentation = False
            else:
                print(char, end='')
