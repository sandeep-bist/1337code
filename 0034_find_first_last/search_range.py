from bisect import bisect, bisect_left
from typing import List

def search_range(nums: List[int], target: int) -> List[int]:
    """
    Time: O(log(n))
    Space: O(1)
    """
    l = bisect_left(nums, target)
    r = bisect(nums, target)
    return [-1, -1] if l == r else [l, r - 1]