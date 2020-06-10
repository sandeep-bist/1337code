from bisect import bisect_left
from typing import List


def search_insert(nums: List, target: int) -> int:
    """
    Time: O(log(n))
    Space: O(1)
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


def search_insert_bisect(nums: List[int], target: int) -> int:
    return bisect_left(nums, target)
