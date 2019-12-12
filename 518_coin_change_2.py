from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    You are given coins of different denominations and a total amount of money.
    Write a function to compute the number of combinations that make up that amount.
    You may assume that you have infinite number of each kind of coin.
    """
    dp = [[0] * (amount + 1) for x in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        # Set the subproblem for the amount of 0 to 1 when solving this row.
        dp[i][0] = 1
        for j in range(1, (amount + 1)):
            current_coin_value = coins[i - 1]
            # dp[i][j] will be the sum of the ways to make change not considering
            # this coin (dp[i-1][j]) and the ways to make change considering this
            # coin (dp[i][j] - currentCoinValue] ONLY if currentCoinValue <= j, otherwise
            # this coin can not contribute to the total # of ways to make change at this
            # sub problem target amount).
            without_this_coin = dp[i - 1][j]
            if current_coin_value <= j:
                with_this_coin = dp[i][j - current_coin_value]
            else:
                with_this_coin = 0
            dp[i][j] = without_this_coin + with_this_coin
    # The answer considering ALL coins for the FULL amount is what
    # we want to return as the answer.
    return dp[len(coins)][amount]


print(change(0, []))  # 1
print(change(5, [1, 5, 10, 25]))  # 2
print(change(10, [1, 5, 10, 25]))  # 4
print(change(25, [1, 5, 10, 25]))  # 13
