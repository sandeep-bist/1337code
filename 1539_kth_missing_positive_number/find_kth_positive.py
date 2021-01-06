from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) / 2
        if arr[m] - 1 - m < k:
            l = m + 1
        else:
            r = m
    return l + k