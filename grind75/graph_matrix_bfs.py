# Shortest path from top left to bottom right
# grid = [[0,0,0,0],
#         [1,1,0,0],
#         [0,0,0,1],
#         [0,1,0,0]]
# visit = {(row#,col#),...}
from collections import deque


# think of bfs as a "layer"
# time complexity is of O(row*col) as we are visiting each node exactly once
def bfs(grid):
    row_length, col_length = len(grid), len(grid[0])
    visit = set()
    queue = deque()  # the current layer we are at
    queue.append((0, 0))  # layer 1 a.k.a the root
    visit.add((0, 0))
    length = 0  # length of the path

    # while we still have elements to traverse
    while queue:
        for i in range(len(queue)):
            row, col = queue.popleft()
            # we have visited all the nodes
            if row == row_length - 1 and col == col_length - 1:
                return length
            # represent directions.
            # [0,1] -> right, [0,-1] -> left, [1,0] -> down, [-1,0] -> up
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for delta_row, delta_col in directions:
                # check if out of bounds or if the cell has been visited or is traversable.
                if (min(row + delta_row, col + delta_col) < 0 or
                        row + delta_row == row_length or
                        col + delta_col == col_length or
                        (row + delta_row, col + delta_col) in visit or
                        grid[row + delta_row][col + delta_col] == 1):
                    continue

                # add each neighbour seen to the queue of things to traverse.
                # This keeps our traversal in order of what directions we have as anything "new" will be added to
                # the end. In other words, this is how we build our layers
                queue.append((row + delta_row, col + delta_col))
                # we are now done with the current node so we can mark it as visited so we don't traverse it again
                visit.add((row + delta_row, col + delta_col))
        length += 1
    return length


if __name__ == '__main__':
    grid = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
    print(bfs(grid))
