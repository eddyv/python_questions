from collections import defaultdict
from typing import Dict

down = (1, 0)
right = (0, 1)
moves = [down, right]


# O(2^n*m)
def count_path_brute_force(row, col, rows, cols):
    # out of bounds
    if row == rows or col == cols:
        return 0
    # last cell
    if row == rows - 1 and col == cols - 1:
        return 1
    return count_path_brute_force(row + 1, col, rows, cols) + count_path_brute_force(row, col + 1, rows, cols)


# O(n*m)
def count_path_dp(row, col, rows, cols, cache):
    # out of bounds
    if row == rows or col == cols:
        return 0
    # last cell
    if row == rows - 1 and col == cols - 1:
        return 1
    # this cell already knows how many paths we can find from it
    if cache[row][col] > 0:
        return cache[row][col]

    cache[row][col] = count_path_dp(row + 1, col, rows, cols, cache) + count_path_dp(row, col + 1, rows, cols, cache)
    return cache[row][col]


def count_path_dp_bottom_up(rows, cols):
    prevRow = [0] * cols

    for r in range(rows - 1, -1, -1):
        currRow = [0] * cols
        # the entire right side of the grid is always 1 cause there's only one path
        currRow[cols - 1] = 1
        # range(start,stop,step)
        # go from the second rightmost column to the leftmost column
        for c in range(cols - 2, -1, -1):
            # add the right cell and the bottom cell
            currRow[c] = currRow[c + 1] + prevRow[c]
        prevRow = currRow
    return prevRow[0]


if __name__ == '__main__':
    grid = [[0] * 60 for i in range(60)]
    print(count_path_dp(0, 0, 60, 60, grid))
    print(count_path_dp_bottom_up(60, 60))
# print(count_path_brute_force(0, 0, 60, 60))
