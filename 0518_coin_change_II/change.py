from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amount + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amount]
