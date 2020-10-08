#!/usr/bin/python3
''' I/O module '''


def pascal_triangle(n):
    ''' Returns a list of lists of integers representing
        the Pascal’s triangle of n.
    '''

    if n <= 0:
        return []
    p_tri = []
    for row in range(n + 1):
        row_list = []
        for col in range(row):
            if col == 0 or col == row - 1:
                row_list.append(1)
            else:
                row_list.append(p_tri[row - 1][col - 1] + p_tri[row - 1][col])
        p_tri.append(row_list)
    return p_tri[1:]
