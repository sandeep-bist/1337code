from heapq import heappushpop, heappush
from typing import List


def k_closest(points: List[List[int]], K: int) -> List[List[int]]:
    """
    Time: O(n * log(k))
    Space: O(k)
    """
    heap = []
    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == K:
            heappushpop(heap, (dist, x, y))
        else:
            heappush(heap, (dist, x, y))
    return [(x, y) for (dist, x, y) in heap]
