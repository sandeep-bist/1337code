from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Given a 2d grid map of '1's (land) and '0's (water), count the number of
    islands. An island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically. You may assume all four edges
    of the grid are all surrounded by water.
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
    """
    Depth-first search.
    """
    if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])
            or grid[row][col] == "0"):
        return
    grid[row][col] = "0"
    dfs(grid, row + 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row - 1, col)
    dfs(grid, row, col - 1)
    return 1


"""
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3
"""
