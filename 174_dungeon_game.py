from typing import List


def calculate_minimum_hp(dungeon: List[List[int]]) -> int:
    """
    The demons had captured the princess (P) and imprisoned her in the
    bottom-right corner of a dungeon. The dungeon consists of M x N rooms
    laid out in a 2D grid. Our valiant knight (K) was initially positioned
    in the top-left room and must fight his way through the dungeon to
    rescue the princess.
    The knight has an initial health point represented by a positive integer.
    If at any point his health point drops to 0 or below, he dies immediately.
    Some of the rooms are guarded by demons, so the knight loses health
    (negative integers) upon entering these rooms; other rooms are either
    empty (0's) or contain magic orbs that increase the knight's health
    (positive integers).
    In order to reach the princess as quickly as possible, the knight decides
    to move only rightward or downward in each step.
    Write a function to determine the knight's minimum initial health so that
    he is able to rescue the princess.
    """
    row, col = len(dungeon), len(dungeon[0])
    dp = [[float("inf") for _ in range(col + 1)] for _ in range(row + 1)]
    dp[row - 1][col] = dp[row][col - 1] = 1
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

    return dp[0][0]


print(calculate_minimum_hp([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
"""
[
  [7, 5, 2, inf],
  [6, 11, 5, inf],
  [1, 1, 6, 1],
  [inf, inf, 1, inf]
]
"""
