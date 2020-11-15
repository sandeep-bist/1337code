from typing import List


def removeInterval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    A, B = toBeRemoved
    for a, b in intervals:
        if a < A:
            res += [a, min(b, A)],
        if b > B:
            res += [max(a, B), b],
    return res