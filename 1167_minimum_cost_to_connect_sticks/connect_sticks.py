import heapq
from typing import List


def connect_sticks(sticks: List[int]) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    heapq.heapify(sticks)
    res = 0
    while len(sticks) > 1:
        f, s = heapq.heappop(sticks), heapq.heappop(sticks)
        tmp = f + s
        res += tmp
        heapq.heappush(sticks, tmp)
    return res
