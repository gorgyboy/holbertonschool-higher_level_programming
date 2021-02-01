#!/usr/bin/python3
'''Python Network 0 module'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''

    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]

    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i+1]:
                peak = list_of_integers[i]
        else:
            if i < len(list_of_integers)-1:
                if list_of_integers[i] >= all([list_of_integers[i-1],
                                               list_of_integers[i+1]]):
                    if list_of_integers[i] > peak:
                        peak = list_of_integers[i]

            elif list_of_integers[i] >= list_of_integers[i-1]:
                if list_of_integers[i] > peak:
                    peak = list_of_integers[i]
    return peak
