#!/usr/bin/python3
'''Python Network 0 module - Task 6'''


def find_peak(list_of_integers):
    '''Wrapper method to find a peak in a list of unsorted integers'''

    size = len(list_of_integers)

    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]
    return search_list_for_peak(list_of_integers, 0, size - 1, size)


def search_list_for_peak(list_int, bottom, top, size):
    '''Finds and returns ta peak element using an adapted binary search'''

    middle = int((bottom + top) / 2)

    # if middle is 0, then middle - 1 is false, so we're at the beginning.
    # if middle is size - 1, then middle + 1 is false, so we're at the end.
    # if we're at either end, we check for peak.
    # else, if we're not at either end, then we check if middle is peak with
    # the list.
    if (middle == 0 or list_int[middle] >= list_int[middle - 1]) and \
            (middle == size - 1 or list_int[middle] >= list_int[middle + 1]):
        return list_int[middle]

    # if we didn't find the peak, we check if the left neighbor is greater than
    # middle.
    # if it is, then we search for the peak in the left side of the list.
    elif middle > 0 and list_int[middle] < list_int[middle - 1]:
        return search_list_for_peak(list_int, bottom, middle - 1, size)

    # otherwise, we search for the peak in the right side of the list.
    else:
        return search_list_for_peak(list_int, middle + 1, top, size)
