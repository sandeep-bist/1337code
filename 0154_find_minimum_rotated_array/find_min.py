from typing import List


def find_min(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid if nums[hi] != nums[mid] else hi - 1
    return nums[lo]
