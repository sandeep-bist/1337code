from typing import List


def maxDistToClosest(seats: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = i = 0
    n = len(seats)
    while i < n:
        while i < n and seats[i]:
            i += 1
        j = i
        while i < n and not seats[i]:
            i += 1
        if not j or i == n:
            res = max(res, i - j)
        else:
            res = max(res, (i - j + 1) // 2)
    return res
