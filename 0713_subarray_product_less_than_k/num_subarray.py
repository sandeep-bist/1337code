from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if k <= 1:
        return 0
    res = left = 0
    p = 1
    for right, e in enumerate(nums):
        p *= e
        while p >= k:
            p /= nums[left]
            left += 1
        res += right - left + 1
    return res
