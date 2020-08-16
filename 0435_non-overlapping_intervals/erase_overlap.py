from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    if not intervals:
        return 0
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    end = sorted_intervals[0][1]
    count = 1
    for interval in sorted_intervals[1:]:
        if interval[0] >= end:
            end = interval[1]
            count += 1
    return len(intervals) - count
