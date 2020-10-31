from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    if not intervals:
        return True
    intervals.sort(key=lambda x: x[0])
    end = intervals[0][1]
    for x,y in intervals[1:]:
        if end > x:
            return False
        end = y
    return True