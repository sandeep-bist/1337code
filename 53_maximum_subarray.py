from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing
    at least one number) which has the largest sum and return its sum.
    """
    if not len(nums):
        return 0
    max_so_far = max_curr = nums[0]
    for i in nums[1:]:
        max_curr = max(i, i + max_curr)
        max_so_far = max(max_so_far, max_curr)
    return max_so_far


def max_sub_array_kadane(nums: List[int]) -> int:
    """
    Alternate solution that modifies array as you iterate.
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))  # 6

nums = []
print(max_sub_array(nums))  # 0
