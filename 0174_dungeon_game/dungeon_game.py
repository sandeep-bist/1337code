from typing import List


def calculate_minimum_hp(dungeon: List[List[int]]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    row, col = len(dungeon), len(dungeon[0])
    dp = [[float("inf") for _ in range(col + 1)] for _ in range(row + 1)]
    dp[row - 1][col] = dp[row][col - 1] = 1
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
    return dp[0][0]


"""
[
  [-2, -3, 3],
  [-5, -10, 1],
  [10, 30, -5]
]

==>

[
  [7, 5, 2, inf],
  [6, 11, 5, inf],
  [1, 1, 6, 1],
  [inf, inf, 1, inf]
]
"""
