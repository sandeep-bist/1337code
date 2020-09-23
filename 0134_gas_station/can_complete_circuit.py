from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    pos = curr = total = 0
    for i in range(len(gas)):
        curr += gas[i] - cost[i]
        total += gas[i] - cost[i]
        if curr < 0:
            curr = 0
            pos = i + 1
    return pos if total >= 0 else -1
