from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Say you have an array for which the ith element is the price of a given
    stock on day i. Design an algorithm to find the maximum profit. You may
    complete at most two transactions.
    You may not engage in multiple transactions at the same time (i.e., you
    must sell the stock before you buy again).
    """
    buy1 = buy2 = float("inf")
    sell1 = sell2 = 0
    for i in prices:
        buy1 = min(buy1, i)
        sell1 = max(sell1, i - buy1)
        buy2 = min(buy2, i - sell1)
        sell2 = max(sell2, i - buy2)
    return sell2


arr = [2, 7, 4, 5, 0, 1, 3, 8]
print(maxProfit(arr))  # 13

arr = [2, 24, 4, 19, 6, 4, 3, 22]
print(maxProfit(arr))  # 41
