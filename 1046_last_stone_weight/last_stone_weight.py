from heapq import heapify, heappop, heappush
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    h = [-x for x in stones]
    heapify(h)
    while len(h) > 1:
        s1, s2 = heappop(h), heappop(h)
        if s1 != s2:
            heappush(h, -abs(s1 - s2))
    return 0 if not h else -h[0]
