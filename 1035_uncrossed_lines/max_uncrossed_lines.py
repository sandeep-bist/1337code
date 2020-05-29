from typing import List


def max_uncrossed_lines(A: List[int], B: List[int]) -> int:
    """
    Time: O(n * m)
    Space: O(n * m)
    Bottom up approach.
    """
    A = [0] + A
    B = [0] + B
    m, n = len(A), len(B)
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
