from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Time: O(n)
    Space: O(1)
    """
    lo, hi = 0, len(s) - 1
    while lo < hi:
        s[lo], s[hi] = s[hi], s[lo]
        lo += 1
        hi -= 1
