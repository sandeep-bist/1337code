from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    if not len(nums):
        return 0
    max_so_far = max_curr = nums[0]
    for i in nums[1:]:
        max_curr = max(i, i + max_curr)
        max_so_far = max(max_so_far, max_curr)
    return max_so_far


def max_subarray_kadane(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)
