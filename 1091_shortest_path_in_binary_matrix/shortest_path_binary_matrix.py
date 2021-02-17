from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    """
    Time: O(n**2)
    Space: O(n)
    """
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]:
        return -1
    seen = set()
    paths = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    queue = deque([(0, 0, 1)])
    seen.add((0, 0))
    while queue:
        num = len(queue)
        for _ in range(num):
            x, y, curr = queue.popleft()
            if x == n - 1 and y == n - 1:
                return curr
            for path in paths:
                i, j = x + path[0], y + path[1]
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i, j) not in seen:
                    seen.add((i, j))
                    queue.append((i, j, curr + 1))
    return -1
            
    