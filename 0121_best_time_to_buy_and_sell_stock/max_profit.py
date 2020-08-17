from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    min_price = float("inf")
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit
