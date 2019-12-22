from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Say you have an array for which the ith element is the price of a given
    stock on day i.
    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (i.e., buy one and sell one share of the stock
    multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e.,
    you must sell the stock before you buy again).
    """
    profits = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profits += prices[i] - prices[i - 1]
    return profits


arr = [7, 1, 5, 3, 6, 4]
print(max_profit(arr))  # 7

arr2 = [7, 6, 5, 4, 3, 2]
print(max_profit(arr2))  # 0

arr3 = [1, 2, 3, 4, 5]
print(max_profit(arr3))  # 4
