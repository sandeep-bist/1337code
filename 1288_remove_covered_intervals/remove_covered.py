from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    intervals.sort(key=lambda x: (x[0], -x[1]))
    end = res = 0
    for _, y in intervals:
        if y > end:
            res += 1
            end = y
    return res
