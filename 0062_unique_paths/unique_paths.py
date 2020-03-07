def unique_paths(m: int, n: int) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    dp = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
