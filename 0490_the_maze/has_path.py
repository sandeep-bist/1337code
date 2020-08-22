from collections import deque
from typing import List


def has_path(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """
    Time: O(n * m)
    Space: O(n * m)
    """
    n, m = len(maze), len(maze[0])
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        if x == destination[0] and y == destination[1]:
            return True
        maze[x][y] = 2
        for i, j in dirs:
            r, c = x, y
            while n > r >= 0 and m > c >= 0 and maze[r][c] != 1:
                r, c = r + i, c + j
            r, c = r - i, c - j
            if maze[r][c] == 0:
                queue.append([r, c])
    return False
