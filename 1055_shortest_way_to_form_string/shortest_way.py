from bisect import bisect_left
from collections import defaultdict


def shortest_way(source: str, target: str) -> int:
    """
    Time: O(m + n * log(m))
    Space: O(n)
    """
    m = defaultdict(list)
    for i, ch in enumerate(source):
        m[ch].append(i)
    res = 1
    i = -1
    for ch in target:
        if ch not in m:
            return -1
        indexes = m[ch]
        # binary search for index
        j = bisect_left(indexes, i)
        if j == len(indexes):
            res += 1
            i = indexes[0] + 1
        else:
            i = indexes[j] + 1
    return res
