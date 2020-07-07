from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Time: O(m * n)
    Space: O(1)
    """
    r, c, res = len(grid), len(grid[0]), 0
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                res += 4
                if i and grid[i - 1][j]:
                    res -= 2
                if j and grid[i][j - 1]:
                    res -= 2
    return res
