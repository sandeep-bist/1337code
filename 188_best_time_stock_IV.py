from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    """
    Say you have an array for which the i-th element is the price of a given
    stock on day i. Design an algorithm to find the maximum profit. You may
    complete at most k transactions.
    You may not engage in multiple transactions at the same time (ie, you must
    sell the stock before you buy again).
    """
    if not prices:
        return 0
    if k >= len(prices) // 2:
        return sum(
            x - y
            for x, y in zip(prices[1:], prices[:-1])
            if x > y)
    profits = [0] * len(prices)
    for _ in range(k):
        preprofit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            preprofit = max(preprofit + profit, profits[i])
            profits[i] = max(profits[i - 1], preprofit)
    return profits[-1]


arr = [2, 7, 4, 5, 0, 1, 3, 8]
print(maxProfit(3, arr))  # 14
print(maxProfit(2, arr))  # 13
print(maxProfit(1, arr))  # 8
