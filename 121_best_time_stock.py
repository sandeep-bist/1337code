from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Say you have an array for which the ith element is the price of a given
    stock on day i. If you were only permitted to complete at most one
    transaction (i.e., buy one and sell one share of the stock), design an
    algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.
    """
    min_price = float("inf")
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit


arr = [7, 1, 5, 3, 6, 4]  # 5
print(maxProfit(arr))

arr2 = [7, 5, 4, 3, 2, 1]  # 0
print(maxProfit(arr2))

arr3 = [2, 4, 1, 2]  # 2
print(maxProfit(arr3))
