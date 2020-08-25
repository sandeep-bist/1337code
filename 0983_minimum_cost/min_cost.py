from typing import List


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    """
    Time: O(m) where m is the max travel date
    Space: O(m)
    """
    last_day = days[-1]
    is_travel_days = set([d for d in days])
    dp = [0] * (last_day + 1)
    for i in range(1, last_day + 1):
        if i not in is_travel_days:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[i - 1] + costs[0],
                        dp[max(i - 7, 0)] + costs[1],
                        dp[max(i - 30, 0)] + costs[2])
    return dp[-1]
