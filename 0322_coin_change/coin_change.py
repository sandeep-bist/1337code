from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Time: O(n * S) where S is the amount
    Space: O(S)
    """
    dp = [0] + [float("inf")] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
