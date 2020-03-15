from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time: O(n log(n))
    Space: O(n)
    """
    intervals.sort(key=lambda x: x[0])
    res = []
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(i[1], res[-1][1])
    return res
