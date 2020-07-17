from collections import Counter
from heapq import heapify, heappop
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    h = [(-y, x) for x, y in Counter(nums).items()]
    heapify(h)
    res = []
    while k:
        res.append(heappop(h)[1])
        k -= 1
    return res
