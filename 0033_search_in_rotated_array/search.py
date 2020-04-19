from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    return helper(nums, 0, len(nums) - 1, target)


def helper(nums: List[int], i: int, j: int, target: int):
    if i > j:
        return -1
    m = (i + j) // 2
    start, mid, end = nums[i], nums[m], nums[j]
    if target == mid:
        return m
    if start < mid:
        if mid > target >= start:
            return helper(nums, i, m - 1, target)
        else:
            return helper(nums, m + 1, j, target)
    elif start > mid:
        if end >= target > mid:
            return helper(nums, m + 1, j, target)
        else:
            return helper(nums, i, m - 1, target)
    else:
        left = helper(nums, i, m - 1, target)
        if left == -1:
            return helper(nums, m + 1, j, target)
        return -1
