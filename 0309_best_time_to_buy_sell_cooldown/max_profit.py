from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
    for p in prices:
        hold = max(hold, notHold - p)
        notHold = max(notHold, notHold_cooldown)
        notHold_cooldown = hold + p
    return max(notHold, notHold_cooldown)
