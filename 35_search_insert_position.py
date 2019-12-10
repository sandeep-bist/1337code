from typing import List


def searchInsert(nums: List, target: int) -> int:
    """
    Given a sorted array and a target value, return the index if the target
    is found. If not, return the index where it would be if it were inserted
    in order.
    You may assume no duplicates in the array.
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


arr = [1, 4, 6, 7]
print(searchInsert(arr, 5))  # 2
print(searchInsert(arr, 8))  # 4
arr = [1]
print(searchInsert(arr, 2))  # 1
arr = [1, 5, 8, 9]
print(searchInsert(arr, 8))  # 2
arr = [1, 3, 5, 6]
print(searchInsert(arr, 5))  # 2
