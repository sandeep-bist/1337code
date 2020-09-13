from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []
    i, n = 0, len(intervals)
    start, end = newInterval
    while i < n and intervals[i][1] < start:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    res.append([start, end])
    while i < n and intervals[i][0] > end:
        res.append(intervals[i])
        i += 1
    return res
