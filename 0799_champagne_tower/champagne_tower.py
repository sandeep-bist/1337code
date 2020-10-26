def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    """
    Time: O(r * c)
    Space: O(r)
    """
    dp = [poured] + [0] * (query_row + 1)
    for i in range(1, query_row + 1):
        for j in range(i, -1, -1):
            dp[j] = max(0, (dp[j] - 1)/2)
            dp[j + 1] += dp[j]
    return min(1, dp[query_glass])
