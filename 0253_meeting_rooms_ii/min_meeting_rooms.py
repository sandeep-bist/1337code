from heapq import heappush, heappop
from typing import List


def minMeetingRooms(intervals: List[List[int]]) -> int:
    """
    Time: O(n * log(n))
    Space: O(n)
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    rooms = []
    heappush(rooms, intervals[0][1])
    for x, y in intervals[1:]:
        if rooms[0] <= x:
            heappop(rooms)
        heappush(rooms, y)
    return len(rooms)
