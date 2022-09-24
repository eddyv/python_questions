# Count paths (backtracking)
# grid = [[0,0,0,0],
#         [1,1,0,0],
#         [0,0,0,1],
#         [0,1,0,0]]
# visit = {(row#,col#),...}
def dfs(grid, row, col, visit):
    row_length, col_length = len(grid), len(grid[0])
    # Check if out of bounds or if the row is not traversable / visited already in the current path.
    if (min(row, col) < 0 or
            row == row_length or col == col_length
            or (row, col) in visit or grid[row][col] == 1):
        return 0
    # check if at the end
    if row == row_length - 1 and col == col_length - 1:
        return 1
    visit.add((row, col))
    count = 0
    # move down
    count += dfs(grid, row + 1, col, visit)
    # move up
    count += dfs(grid, row - 1, col, visit)
    # move right
    count += dfs(grid, row, col + 1, visit)
    # move left
    count += dfs(grid, row, col - 1, visit)
    visit.remove((row, col))
    return count


if __name__ == '__main__':
    grid = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
    print(dfs(grid, 3, 0, set()))
    print(dfs(grid, 0, 3, set()))
    print(dfs(grid, 0, 0, set()))
