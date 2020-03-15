from collections import Counter
import heapq
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """
    Space: O(n)
    Time: O(n)
    """
    h = [(-y, x) for x, y in Counter(tasks).items()]
    heapq.heapify(h)
    res = 0
    while h:
        i, tmp = 0, []
        while i <= n:
            res += 1
            if h:
                count, letter = heapq.heappop(h)
                count += 1
                if count:
                    tmp.append((count, letter))
            if not h and not tmp:
                break
            i += 1
        for item in tmp:
            heapq.heappush(h, item)
    return res


def least_interval_math(tasks: List[str], n: int) -> int:
    """
    Space: O(n)
    Time: O(n)
    """
    c = Counter(tasks)
    m = max(c.values())
    res = (m - 1) * (n + 1)
    for v in c.values():
        if v == m:
            res += 1
    return max(res, len(tasks))
