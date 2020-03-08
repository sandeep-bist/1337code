from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
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
