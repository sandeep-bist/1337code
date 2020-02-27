from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    In a given grid, each cell can have one of three values:
    - the value 0 representing an empty cell;
    - the value 1 representing a fresh orange;
    - the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a
    rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has
    a fresh orange.  If this is impossible, return -1 instead.
    """
    n, m = len(grid), len(grid[0])
    rotten = deque()
    fresh = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                rotten.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    minutes = 0
    while rotten:
        for _ in range(len(rotten)):
            i, j = rotten.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                    fresh -= 1
                    rotten.append((x, y))
                    grid[x][y] = 2
        minutes += 1
    return max(0, minutes - 1) if not fresh else -1


grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(oranges_rotting(grid1))  # 4

grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(oranges_rotting(grid2))  # -1

grid3 = [[0, 2]]
print(oranges_rotting(grid3))  # 0
