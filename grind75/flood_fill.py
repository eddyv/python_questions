from collections import deque
from typing import List


# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
# to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
# to those pixels (also with the same color), and so on. Replace the color of all the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    row_length, col_length = len(image), len(image[0])
    visit = set()
    queue = deque()
    start_color = image[sr][sc]
    queue.append((sr, sc))
    visit.add((sr, sc))

    while queue:
        for i in range(len(queue)):
            row, col = queue.popleft()
            # [0,1] -> right, [0,-1] -> left, [1,0] -> down, [-1,0] -> up
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # set the new color to the cell
            image[row][col] = color
            for delta_row, delta_col in directions:
                # base case
                # if out of bounds or if the color isn't a starting color or if we have visited the node already
                if min(row + delta_row,
                       col + delta_col) < 0 or row + delta_row == row_length or col + delta_col == col_length or \
                        image[row + delta_row][col + delta_col] != start_color or \
                        (row + delta_row, col + delta_col) in visit:
                    continue
                queue.append((row + delta_row, col + delta_col))
                visit.add((row, col))
    return image


if __name__ == '__main__':
    image = [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(image, sr, sc, color))
    image = [[0, 0, 0],
             [0, 0, 0]]
    sr = 0
    sc = 0
    color = 0
    print(floodFill(image, sr, sc, color))
