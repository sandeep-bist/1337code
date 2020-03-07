from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    if not len(grid):
        return 0
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                islands += dfs(grid, i, j)
    return islands


def dfs(grid: List[List[str]], row: int, col: int) -> int:
    if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
            or grid[row][col] == "0"):
        return
    grid[row][col] = "0"
    dfs(grid, row + 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row - 1, col)
    dfs(grid, row, col - 1)
    return 1
