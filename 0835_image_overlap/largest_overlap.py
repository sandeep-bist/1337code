from collections import defaultdict
from typing import List


def largest_overlap(A: List[List[int]], B: List[List[int]]) -> int:
    """
    Time: O(n**4)
    Space: O(n**2)
    """
    a, b = [], []
    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c] == 1:
                a.append((r, c))
            if B[r][c] == 1:
                b.append((r, c))
    d = defaultdict(int)
    res = 0
    for x1, y1 in a:
        for x2, y2, in b:
            vector = (x2-x1, y2-y1)
            d[vector] += 1
            res = max(res, d[vector])
    return res
