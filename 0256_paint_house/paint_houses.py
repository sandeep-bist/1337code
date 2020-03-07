from typing import List


def min_cost(costs: List[List[int]]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if not costs:
        return 0
    for i in range(1, len(costs)):
        prev = costs[i - 1]
        costs[i][0] += min(prev[1], prev[2])
        costs[i][1] += min(prev[0], prev[2])
        costs[i][2] += min(prev[0], prev[1])
    return min(costs[len(costs) - 1])
