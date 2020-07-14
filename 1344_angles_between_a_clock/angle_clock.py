def angle_clock(hour: int, minutes: int) -> float:
    """
    Time: O(1)
    Space: O(1)
    """
    h = ((360/12) * hour) + (360/12/60) * minutes
    m = (360/60) * minutes
    diff = abs(h - m)
    return diff if diff <= 180 else 360 - diff
