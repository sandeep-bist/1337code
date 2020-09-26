from typing import List


def find_poisoned_duration(timeSeries: List[int], duration: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if not timeSeries:
        return 0
    res = 0
    for i in range(len(timeSeries) - 1):
        res += min(timeSeries[i + 1] - timeSeries[i], duration)
    return res + duration
