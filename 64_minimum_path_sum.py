from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    Given a m x n grid filled with non-negative numbers, find a path from
    top left to bottom right which minimizes the sum of all numbers along
    its path.
    You can only move either down or right at any point in time.
    O(n * m) space. Can optimize for O(1) if one modifies given matrix.
    """
    r, c = len(grid), len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = grid[0][0]
    for i in range(1, r):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, c):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j - 1])
    return dp[-1][-1]


matrix = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(min_path_sum(matrix)) # 7
