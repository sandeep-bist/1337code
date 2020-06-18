from typing import List


def h_index(citations: List[int]) -> int:
    """
    Time: O(log(n))
    Space:(1)
    """
    size = len(citations)
    lo, hi = 0, size - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        m_val = citations[mid]
        c = size - mid
        if m_val == c:
            return c
        if m_val < c:
            lo = mid + 1
        else:
            hi = mid - 1
    return size - lo
