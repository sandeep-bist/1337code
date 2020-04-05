from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    profits = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profits += prices[i] - prices[i - 1]
    return profits
