from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    buy1 = buy2 = float("inf")
    sell1 = sell2 = 0
    for i in prices:
        buy1 = min(buy1, i)
        sell1 = max(sell1, i - buy1)
        buy2 = min(buy2, i - sell1)
        sell2 = max(sell2, i - buy2)
    return sell2
