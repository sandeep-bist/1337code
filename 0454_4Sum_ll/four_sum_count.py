from collections import defaultdict
from typing import List


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    """
    Time: O(n ** 2)
    Space: O(n)
    """
    counts = defaultdict(int)
    res = 0
    for c in C:
        for d in D:
            sub = c + d
            counts[sub] += 1
    for a in A:
        for b in B:
            sub = a + b
            res += counts[sub * -1]
    return res
            