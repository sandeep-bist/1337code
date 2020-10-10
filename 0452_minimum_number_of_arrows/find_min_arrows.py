from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    """
    Time: O(n * log(n))
    Space: O(1)
    """
    if not points:
        return 0
    res = 1
    points.sort(key=lambda x: x[1])
    end = points[0][1]
    for x, y in points:
        if x > end:
            res += 1
            end = y
    return res
