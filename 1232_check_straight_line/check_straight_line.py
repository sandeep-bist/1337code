from typing import List


def check_straight_line(coordinates: List[List[int]]) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    (x0, y0), (x1, y1) = coordinates[:2]
    dx, dy = x1 - x0, y1 - y0
    # slope is dx / dy
    for (x, y) in coordinates:
        if (x - x1) * dy != (y - y1) * dx:
            return False
    return True
