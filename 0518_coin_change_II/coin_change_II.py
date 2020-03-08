from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    dp = [[0] * (amount + 1) for x in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1
        for j in range(1, (amount + 1)):
            current_coin_value = coins[i - 1]
            without_this_coin = dp[i - 1][j]
            if current_coin_value <= j:
                with_this_coin = dp[i][j - current_coin_value]
            else:
                with_this_coin = 0
            dp[i][j] = without_this_coin + with_this_coin
    return dp[len(coins)][amount]
