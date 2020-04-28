def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(text1) + 1, len(text2) + 1
    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
        