from typing import List


def single_nonduplicate(nums: List[int]) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        if mid & 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            start = mid + 2
        else:
            end = mid
    return nums[start]
