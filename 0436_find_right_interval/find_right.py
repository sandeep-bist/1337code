from typing import List


def find_right_interval(intervals: List[List[int]]) -> List[int]:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    l = sorted((start, i) for i, (start, _) in enumerate(intervals))
    res = []
    for _, end in intervals:
        r = bisect.bisect_left(l, (end,))
        res.append(l[r][1] if r < len(l) else -1)
    return res
