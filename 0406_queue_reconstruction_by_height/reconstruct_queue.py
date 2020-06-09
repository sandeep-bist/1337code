from heapq import heapify, heappush, heappop
from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    """
    Time: O(n**2)
    Space: O(n)
    """
    heap = [(-x, y) for x, y in people]
    heapify(heap)
    res = []
    while heap:
        height, index = heappop(heap)
        res.insert(index, [-height, index])
    return res
