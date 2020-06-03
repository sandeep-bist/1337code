from typing import List


def two_city_sched_cost(costs: List[List[int]]) -> int:
    """
    Time: (O n * log(n))
    Space: O(1)
    """
    costs.sort(key=lambda x: x[0] - x[1])
    total = 0
    n = len(costs) // 2
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    return total
